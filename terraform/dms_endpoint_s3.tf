/* 
  Manually created mer-dmscdc-s3-target-manual
	due to 
    https://github.com/hashicorp/terraform-provider-aws/issues/12584

resource "aws_dms_endpoint" "mer-dmscdc-s3-target-endpoint" {
  endpoint_id                 = "mer-dmscdc-s3-target-endpoint"
  endpoint_type               = "target"
  engine_name                 = "s3"
  //service_access_role         = "${aws_iam_role.dms-access-for-endpoint.arn}"
  service_access_role_arn     = "arn:aws:iam::393895250050:role/dms-access-for-endpoint"
  s3_settings {
      bucket_name             = "${aws_s3_bucket.mer-dmscdc-bucket.id}"
      add_column_name         = "true"
      cdc_inserts_and_updates = "true"
  }
}

# Manual creation example
aws dms create-endpoint --endpoint-identifier mer-dmscdc-s3-target-manual --engine-name s3 --endpoint-type target --s3-settings '{"ServiceAccessRoleArn": "arn:aws:iam::393895250050:role/dms-access-for-endpoint", "BucketName": mer-dmscdc-nyapzhvfbh-bucket, "DataFormat": "csv","add_column_name":"true","cdc_inserts_and_updates":"true"}'

*/