output "CICD_Repo HTTP URL" {
  value = "${aws_codecommit_repository.repo.clone_url_http}"
}

output "CICD_Repo SSH URL" {
  value = "${aws_codecommit_repository.repo.clone_url_ssh}"
}

output "CICD_Artifact Bucket" {
  value = "${aws_s3_bucket.build_artifact_bucket.id}"
}