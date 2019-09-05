# waf variables
variable "domain_name" {
  description = "The domain name of the site that will be created in imperva"
  default = "www.api-np.anz"
}

variable "account_id" {
  description = "Imperva sub-account id"
  default = ""
}
variable "whitelist_ips" {
  description = "The IP address to be allowed in the site"
  default = "1.136.105.74/32,1.152.105.189/32,203.110.235.143/32,49.255.135.34/32"
}

variable "blacklist_ips" {
  description = "Default should be 0.0.0.0/0 to not allow ant IPs except in the whitelist ips"
  default = "0.0.0.0/0"
}

variable "rewrite_to" {
  description = "The TO in rewrite rule of header"
  default = "forgerock-unauth-sit.sec.gcpnp.anz"
}

variable "rewrite_from" {
  description = "The FROM in rewrite rule of header"
  default = "api-np.anz"
}

variable "rewrite_name" {
  description = "The header name that will be rewrite or change to"
  default = "Host"
}
