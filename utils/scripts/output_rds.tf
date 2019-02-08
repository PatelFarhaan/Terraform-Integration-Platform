output "RDS_Endpoint" {
  description = "EndPoint"
  value       = "${aws_db_instance.rds.endpoint}"
}

output "RDS_Database Name" {
  description = "Name"
  value       = "${aws_db_instance.rds.name}"
}

output "RDS_User Name" {
  description = "Username"
  value       = "${aws_db_instance.rds.username}"
}


