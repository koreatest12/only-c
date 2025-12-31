# ---------------------------------------------------------
# 1. OIDC 공급자 생성 (에러 해결의 핵심)
# ---------------------------------------------------------
resource "aws_iam_openid_connect_provider" "github" {
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  # GitHub의 공식 OIDC 지문(Thumbprint)입니다. (고정값)
  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

# ---------------------------------------------------------
# 2. GitHub Actions가 사용할 역할(Role) 생성
# ---------------------------------------------------------
resource "aws_iam_role" "github_action_role" {
  name = "GitHubAction-Infra-Role"

  # 신뢰 관계 정책 (GitHub의 특정 리포지토리만 접속 허용)
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRoleWithWebIdentity"
        Effect = "Allow"
        Principal = {
          Federated = aws_iam_openid_connect_provider.github.arn
        }
        Condition = {
          StringLike = {
            # [중요] 본인의 ID와 리포지토리명으로 정확히 제한
            "token.actions.githubusercontent.com:sub": "repo:koreatest12/only-c:*"
          }
        }
      }
    ]
  })
}

# ---------------------------------------------------------
# 3. 역할에 권한 부여 (DB, EC2 등을 생성할 수 있는 권한)
# ---------------------------------------------------------
resource "aws_iam_role_policy" "github_action_policy" {
  name = "GitHubAction-Infra-Policy"
  role = aws_iam_role.github_action_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ec2:*",
          "rds:*",
          "s3:*",
          "iam:*",
          "dynamodb:*"
        ]
        Resource = "*"
      }
    ]
  })
}

# ---------------------------------------------------------
# 4. 출력값 (워크플로우에 넣을 Role ARN 확인용)
# ---------------------------------------------------------
output "role_arn" {
  value       = aws_iam_role.github_action_role.arn
  description = "GitHub Actions 워크플로우 파일에 붙여넣을 ARN"
}
