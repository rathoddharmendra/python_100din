provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "frankfurt_api" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  user_data     = file("${path.module}/userdata.sh")
  tags = {
    Name = "FrankfurtAPI"
  }
}

resource "aws_lb" "frankfurt_alb" {
  name               = "frankfurt-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = [/* Add subnet IDs */]
  security_groups    = [/* Add SGs */]
}