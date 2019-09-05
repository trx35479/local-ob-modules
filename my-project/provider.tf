terraform {
  required_version = "0.11.14"

#  backend "gcs" {
#    prefix = "network/infra/"
#    bucket = "rowel_uchi_bucket"
#  }
}

provider "google" {
  region  = "${var.region}"
  version = "2.5.1"
}

provider "google-beta" {
  region  = "${var.region}"
  version = "2.5.1"
}