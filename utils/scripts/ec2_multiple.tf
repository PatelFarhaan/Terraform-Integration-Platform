resource "aws_security_group" "ec2" {
  name        = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-sg-ec2"
  description = "EC2 Security Group"
  vpc_id      = "${data.aws_vpc.default.id}"

  # SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP access from the VPC
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_policy" "policy" {
  name        = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-policy"
  policy      = "${file("policys3bucket.json")}"
}

resource "aws_iam_role" "ec2_s3_access_role" {
  name               = "s3-role-${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}"
  assume_role_policy = "${file("assumerolepolicy.json")}"
}

resource "aws_iam_policy_attachment" "attach" {
  name       = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-attachment"
  roles      = ["${aws_iam_role.ec2_s3_access_role.name}"]
  policy_arn = "${aws_iam_policy.policy.arn}"
}

resource "aws_iam_instance_profile" "profile" {
  name  = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}_profile"
  roles = ["${aws_iam_role.ec2_s3_access_role.name}"]
}

resource "aws_security_group" "elb" {
  name        = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-elb"
  description = "Used in the terraform"
  vpc_id      = "${data.aws_vpc.default.id}"

  # HTTP access from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

module "ec2" {
  source = "terraform-aws-modules/ec2-instance/aws"
  instance_count = "${var.ec2_count}"
  name                        = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-ec2"
  ami                         = "${var.ec2_ami}"
  instance_type               = "${var.ec2_instancetype}"
  subnet_id                   = "${element(data.aws_subnet_ids.all.ids, 0)}"
  vpc_security_group_ids      = ["${aws_security_group.ec2.id}"]
  iam_instance_profile = "${aws_iam_instance_profile.profile.name}"
  associate_public_ip_address = "true"
  key_name = "hadoopec2"
  tags {
    AppName = "${var.ec2_appname}"
    Environment = "${var.ec2_environment}"
  }
  user_data = <<EOF
	{
		#!/bin/bash
		yum -y update
		yum install -y ruby
		cd /home/ec2-user
		curl -O https://aws-codedeploy-us-west-2.s3.amazonaws.com/latest/install
		chmod +x ./install
		./install auto
	}
	EOF
}

resource "aws_elb" "web" {
  name = "${var.ec2_appname}-${var.ec2_environment}-${var.ec2_environment_id}-elb"

  subnets        = ["${element(data.aws_subnet_ids.all.ids, 0)}"]
  security_groups = ["${aws_security_group.elb.id}"]
  instances       = ["${module.ec2.id}"]

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }
}