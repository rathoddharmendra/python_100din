provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "mumbai_api" {
  ami           = "ami-03f4878755434977f"
  instance_type = "t2.micro"
  user_data     = file("${path.module}/userdata.sh")
  tags = {
    Name = "MumbaiAPI"
  }
}

resource "aws_lb" "mumbai_alb" {
  name               = "mumbai-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = [/* Add subnet IDs */]
  security_groups    = [/* Add SGs */]
}