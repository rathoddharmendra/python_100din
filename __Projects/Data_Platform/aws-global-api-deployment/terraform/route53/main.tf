resource "aws_route53_record" "frankfurt" {
  zone_id = "YOUR_HOSTED_ZONE_ID"
  name    = "myapi.example.com"
  type    = "A"
  alias {
    name                   = "ALB_Frankfurt_DNS"
    zone_id                = "ALB_ZONE_ID"
    evaluate_target_health = true
  }
  set_identifier = "Frankfurt"
  region         = "eu-central-1"
  latency_routing_policy {}
}

resource "aws_route53_record" "mumbai" {
  zone_id = "YOUR_HOSTED_ZONE_ID"
  name    = "myapi.example.com"
  type    = "A"
  alias {
    name                   = "ALB_Mumbai_DNS"
    zone_id                = "ALB_ZONE_ID"
    evaluate_target_health = true
  }
  set_identifier = "Mumbai"
  region         = "ap-south-1"
  latency_routing_policy {}
}