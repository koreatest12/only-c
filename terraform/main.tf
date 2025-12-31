# 변수 선언
variable "db_storage_size" { default = 20 }
variable "instance_count" { default = 1 }
variable "db_name_prefix" { default = "db-node" }

# [DB 대량 생성 로직]
resource "aws_db_instance" "mass_db" {
  # 입력받은 수량(instance_count)만큼 반복 생성
  count = var.create_db ? var.instance_count : 0
  
  # 이름 뒤에 번호 붙이기 (예: db-main-01, db-main-02 ...)
  identifier = "${var.db_name_prefix}-${format("%02d", count.index + 1)}"
  
  # 입력받은 용량(target_size_gb) 적용
  allocated_storage = var.db_storage_size
  
  instance_class    = "db.t3.micro"
  engine            = "mysql"
  username          = "admin"
  password          = "password1234" # 실제로는 Secrets Manager 사용 권장
  skip_final_snapshot = true
}

# [디스크 대량 추가 로직]
resource "aws_ebs_volume" "mass_disk" {
  count = var.add_new_disk ? var.disk_count : 0

  availability_zone = "ap-northeast-2a"
  
  # 입력받은 용량 적용
  size = var.disk_size
  
  tags = {
    Name = "${var.disk_name_prefix}-${count.index + 1}"
  }
}
