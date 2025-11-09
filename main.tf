# ==========================
# AWS Provider
# ==========================
provider "aws" {
  region = "us-east-1"
}

# ==========================
# S3 Bucket
# ==========================
resource "aws_s3_bucket" "my_bucket" {
  bucket = "jitha-tf-bucket-2025-12345" # Change this to a globally unique name
}

# ==========================
# Security Group
# ==========================
resource "aws_security_group" "my_sg" {
  name        = "terraform-sg"
  description = "Allow SSH and HTTP"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]   # SSH from anywhere (for demo only)
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]   # HTTP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ==========================
# Get Latest Amazon Linux 2 AMI
# ==========================
data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  owners = ["amazon"]
}

# ==========================
# EC2 Instance
# ==========================
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"
  security_groups = [aws_security_group.my_sg.name]

  tags = {
    Name = "TerraformDemoEC2"
  }
}
