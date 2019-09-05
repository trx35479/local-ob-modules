terraform {
  required_version = "0.11.14"

  backend "gcs" {
    prefix = "network/k6"
    bucket = "anz-cs-palo-np-88de38"
  }
}

provider "google" {
  region  = "${var.region}"
  version = "2.5.1"
}

provider "google-beta" {
  region  = "${var.region}"
  version = "2.5.1"
}
