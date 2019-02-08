variable "repo_name" {
  description = "The name of the CodeCommit repository"
  default     = "app1"
}

variable "repo_default_branch" {
  description = "The name of the default repository branch"
  default     = "master"
}

variable "force_artifact_destroy" {
  description = "Force the removal of the artifact S3 bucket on destroy (default: false)."
  default     = "false"
}

variable "s3_artifact_bucket" {
  description = "Artifact Bucket Name"
  default     = "app1"
}

variable "cicd_appname" {
    default = "app1"
}

variable "cicd_env" {
    default = "prod"
}

variable "build_timeout" {
  description = "The time to wait for a CodeBuild to complete before timing out in minutes (default: 5)"
  default     = "5"
}

variable "build_compute_type" {
  description = "The build instance type for CodeBuild (default: BUILD_GENERAL1_SMALL)"
  default     = "BUILD_GENERAL1_SMALL"
}

variable "build_image" {
  description = "The build image for CodeBuild to use (default: aws/codebuild/nodejs:6.3.1)"
  default     = "aws/codebuild/nodejs:6.3.1"
}

variable "build_privileged_override" {
  description = "Set the build privileged override to 'true' if you are not using a CodeBuild supported Docker base image. This is only relevant to building Docker images"
  default     = "false"
}

variable "package_buildspec" {
  description = "The buildspec to be used for the Package stage (default: buildspec.yml)"
  default     = "buildspec.yml"
}

variable "test_buildspec" {
  description = "The buildspec to be used for the Package stage (default: buildspec.yml)"
  default     = "buildspec_test.yml"
}

variable "cicd_env_id" {
    default = "1"
}
