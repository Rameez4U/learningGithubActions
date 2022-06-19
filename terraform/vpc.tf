resource "aws_vpc" "mer-vpc" {
  cidr_block = "10.213.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}
resource "aws_internet_gateway" "mer-ig" {
  vpc_id = "${aws_vpc.mer-vpc.id}"
}

# Grant the VPC internet access on its main route table
resource "aws_route" "internet_access" {
  route_table_id         = "${aws_vpc.mer-vpc.main_route_table_id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = "${aws_internet_gateway.mer-ig.id}"
}

# Create a subnet to launch our instances into
resource "aws_subnet" "mer-subnet-pub-213-101" {
  vpc_id                  = "${aws_vpc.mer-vpc.id}"
  cidr_block              = "10.213.101.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-west-1a"
}

resource "aws_subnet" "mer-subnet-pub-213-102" {
  vpc_id                  = "${aws_vpc.mer-vpc.id}"
  cidr_block              = "10.213.102.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-west-1c"
}

# basic security group
resource "aws_security_group" "basic-sg" {
  name        = "basic-sg"
  description = "MER Basic SG"
  vpc_id      = "${aws_vpc.mer-vpc.id}"
  # SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
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