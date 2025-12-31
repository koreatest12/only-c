# 1. 파일 읽기 및 디코딩
locals {
  # 다운로드된 JSON 파일을 읽어서 객체로 변환
  config_data = jsondecode(file("${path.module}/mass_config.json"))
  
  # DB 목록 추출 (JSON 구조에 따라 조정)
  db_list = try(local.config_data.databases, [])
  
  # 디스크 목록 추출
  disk_list = try(local.config_data.disks, [])
}

variable "action_type" {
  description = "워크플로우에서 선택한 작업 유형"
  type        = string
}

# 2. DB 대량 생성 (다운로드된 정보 기반)
resource "aws_db_instance" "mass_db" {
  # action_type이 create_db일 때만 작동하며, JSON 내의 모든 DB를 순회함
  for_each = var.action_type == "create_db" ? { for db in local.db_list : db.id => db } : {}

  identifier        = each.value.id          # JSON의 id 값 (예: db-main-01)
  allocated_storage = each.value.size_gb     # JSON의 size_gb 값 (예: 100)
  instance_class    = each.value.class       # JSON의 class 값 (예: db.t3.medium)
  engine            = "mysql"
  username          = "admin"
  password          = "password1234"
  skip_final_snapshot = true
  
  tags = {
    Owner = each.value.owner
    Team  = "DevOps"
  }
}

# 3. 디스크 대량 생성
resource "aws_ebs_volume" "mass_disk" {
  for_each = var.action_type == "add_disk" ? { for disk in local.disk_list : disk.id => disk } : {}

  availability_zone = "ap-northeast-2a"
  size              = each.value.size_gb
  
  tags = {
    Name = each.value.id
  }
}
