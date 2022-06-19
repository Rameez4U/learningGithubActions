resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "IncrementalProcess"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "Dimension"
  range_key      = "ModifiedDate"

  attribute {
    name = "Dimension"
    type = "S"
  }

/* Will add as un-indexed value
  attribute {
    name = "createDate"
    type = "N"
  }
*/

  attribute {
    name = "ModifiedDate"
    type = "N"
  }

}