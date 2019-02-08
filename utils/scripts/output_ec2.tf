output "EC2_Server Public DNS" {
  description = "Public DNS of EC2 Instances"
  value       = "${module.ec2.public_dns}"
}

output "EC2_ELB Public Dns" {
  description = "Public DNS of ELB"
  value       = "${aws_elb.web.dns_name}"
}