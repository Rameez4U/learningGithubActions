resource "aws_dms_endpoint" "mer-dmscdc-sqlsvr-source-endpoint" {
  endpoint_id   = "mer-dmscdc-sqlsvr-source-endpoint"
  endpoint_type = "source"
  engine_name   = "sqlserver"
  server_name   = var.sqlsvr_server_name
  database_name = var.sqlsvr_server_db
  username      = var.sqlsvr_username
  password      = var.sqlsvr_password
  port          = "1433"
}