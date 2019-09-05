variable "domain_name" {
  description = "The domain name of the site that will be created in imperva"
  default     = "thecloudnative.io"
}

variable "site_ip" {
  description = "The origin server ip address"
  default     = "grafana.thecloudnative.io"
}

variable "account_id" {
  default = "1367860" // this is the non-prod imperva account
}

variable "certificate" {
  default = "./mydomain.crt"
}

variable "private_key" {
  default = "./mydomain.key"
}

//variable "token" {}

