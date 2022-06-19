variable "sqlsvr_username" {
  description = "SQL Server Database username"
  type        = string
  sensitive   = true
}

variable "sqlsvr_password" {
  description = "SQL Server Database password"
  type        = string
  sensitive   = true
}

variable "sqlsvr_server_name" {
  description = "SQL Server Name"
  type        = string
}

variable "sqlsvr_server_db" {
  description = "SQL Server Database"
  type        = string
}

variable "aws_access_key" {}

variable "aws_secret_key" {}

variable "region" {
        default = "us-west-1"
}

variable "deployment_env" {
  description = "Deployment Environment"
  type        = string

  validation {
    condition = anytrue([
      var.deployment_env == "Sandbox",
      var.deployment_env == "RND",
      var.deployment_env == "Production"
    ])
    error_message = "Variable deployment_env must be one of allowed options."
  }
}
