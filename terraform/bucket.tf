resource "aws_s3_bucket" "mer-dmscdc-bucket" {
  bucket = "mer-dmscdc-nyapzhvfbh-bucket"
}

resource "aws_s3_bucket_acl" "mer-dmscdc-bucket-acl" {
  bucket = aws_s3_bucket.mer-dmscdc-bucket.id
  acl    = "private"
}