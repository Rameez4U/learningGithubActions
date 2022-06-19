terraform {
 backend "s3" {
   bucket         = "mer-s3-tf-state-nyapzhvfbh-bucket"
   key            = "state/terraform.tfstate"
   region         = "us-west-1"
 }
}