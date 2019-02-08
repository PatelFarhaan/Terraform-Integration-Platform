resource "aws_security_group" "rds" {
  name        = "${var.rds_appname}-${var.rds_environment}-sg-rds" 
  description = "RDS Security Group"
  vpc_id      = "${data.aws_vpc.default.id}"

  # HTTP access from anywhere
  ingress {
    from_port   = 3306
    to_port     = 3306
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

resource "aws_db_instance" "rds" {
  allocated_storage    = "${var.rds_storage}"
  storage_type         = "gp2"
  engine               = "${var.rds_engine}"
  identifier		   = "i-${var.rds_environment_id}-id"
  engine_version       = "${var.rds_engine_version}"
  instance_class       = "${var.rds_instance}"
  name                 = "${var.rds_appname}"
  username             = "${var.rds_username}"
  password             = "${var.rds_password}"
  vpc_security_group_ids      = ["${aws_security_group.rds.id}"]
  final_snapshot_identifier = "si-${var.rds_environment_id}-id-final-snapshot"
  publicly_accessible = true
}