# configure the site

resource "incapsula_site" "site" {
  account_id             = "${var.account_id}"
  domain                 = "api.${var.domain_name}"
  send_site_setup_emails = "true"
  site_ip                = "${var.site_ip}"
  force_ssl              = "true"
  log_level              = "full"
}

# Security Rule: Blacklist IP
resource "incapsula_acl_security_rule" "blacklist" {
  rule_id = "api.acl.blacklisted_ips"
  site_id = "${incapsula_site.site.id}"
  ips     = "${var.blacklist_ips}"
}

# Security Rule: Whitelist IP
# append a depends_on attributes for multiple security rule (raise condition issue on api)
resource "incapsula_acl_security_rule" "whitelist" {
  rule_id = "api.acl.whitelisted_ips"
  site_id = "${incapsula_site.site.id}"
  ips     = "${var.whitelist_ips}"

  depends_on = ["incapsula_acl_security_rule.blacklist"]
}

# Block certain countries based on country code
resource "incapsula_acl_security_rule" "countries" {
  rule_id   = "api.acl.blacklisted_countries"
  site_id   = "${incapsula_site.site.id}"
  countries = "${var.block_countries}"

  depends_on = ["incapsula_acl_security_rule.blacklist",
    "incapsula_acl_security_rule.whitelist",
  ]
}

# Blacklist / site and allow only specific url
#resource "incapsula_acl_security_rule" "url" {
#  site_id      = "${incapsula_site.site.id}"
#  rule_id      = "api.acl.blacklisted_urls"
#  urls         = ["/ "]
#  url_patterns = ["PREFIX"]
#}

# Add exception URL (manually add url blacklist as imperva api is buggy if the url is "/")
#resource "incapsula_acl_whitelist_rule" "url-whitelist" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_acl_security_rule.url.rule_id}"
#  urls              = ["/cds-au/v1/banking/products*"]
#  exception_id_only = "true"
#

# Incap Rule: Rewrite Header (ADR)
# the parameter "enabled" can be used to enable "true" or "false" the resource (new feature release v0.6.xx
resource "incapsula_incap_rule" "rewrite-header" {
  priority      = "17"
  name          = "change_host_header"
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REWRITE_HEADER"
  add_missing   = "true"
  from          = "api.${var.domain_name}"
  to            = "${var.rewrite_to}"
  allow_caching = "false"
  rewrite_name  = "${var.rewrite_name}"
  enabled       = "false"
}

# This will redirect all request from http to https
# the parameter "enabled" can be used to enable "true" or "false" the resource (new feature release v0.6.xx
resource "incapsula_incap_rule" "redirect" {
  name          = "redirect_site_to_https"
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REDIRECT"
  priority      = "1"
  response_code = "301"
  from          = "http://api.${var.domain_name}/*"
  to            = "https://api.${var.domain_name}/$1"
  enabled       = "true"
}

# Incap set the cross site scripting to block (the default is alert only)
# append a depends_on attributes for multiple security rule (raise condition issue on api)
resource "incapsula_waf_security" "waf-xss" {
  site_id              = "${incapsula_site.site.id}"
  rule_id              = "api.threats.cross_site_scripting"
  security_rule_action = "api.threats.action.block_request"
}

resource "incapsula_waf_security" "ddos" {
  site_id                = "${incapsula_site.site.id}"
  rule_id                = "api.threats.ddos"
  activation_mode        = "api.threats.ddos.activation_mode.auto"
  ddos_traffic_threshold = "${var.ddos_threshold}"

  depends_on = [
    "incapsula_waf_security.waf-xss",
  ]
}

# Cache resources
resource "incapsula_cache_response_headers" "cacheheaders" {
  site_id       = "${incapsula_site.site.id}"
  cache_headers = ["server", "x-v"]
}

# Cache Mode (no cache, static_only, static_and_dynamic, and aggressive)
resource "incapsula_cache_mode" "cacheMode" {
  site_id    = "${incapsula_site.site.id}"
  cache_mode = "static_only"
}

# Set the Data Storage Region
resource "incapsula_data_storage_region" "data-storage" {
  site_id             = "${incapsula_site.site.id}"
  data_storage_region = "APAC"
}

# This has been created manually
# New feature is available to configure this using terraform provider (v0.6.x)
# the parameter "enabled" can be used to enable "true" or "false" the resource
resource "incapsula_cache_rule" "cache-rule-filter" {
  site_id                 = "${incapsula_site.site.id}"
  name                    = "x-min-v cache key"
  action                  = "HTTP_CACHE_DIFFERENTIATE_BY_HEADER"
  filter                  = "HeaderExists == \"x-min-v\""
  differentiated_by_value = "x-min-v"
  enabled                 = "true"
}

resource "incapsula_cache_rule" "cache-rule-diff" {
  site_id                 = "${incapsula_site.site.id}"
  name                    = "x-v cache key"
  action                  = "HTTP_CACHE_DIFFERENTIATE_BY_HEADER"
  differentiated_by_value = "x-v"
  enabled                 = "true"
}

// do not cache based on headers
resource "incapsula_cache_rule" "no-cache" {
  site_id = "${incapsula_site.site.id}"
  name    = "no-cache-header"
  action  = "HTTP_CACHE_FORCE_UNCACHEABLE"
  filter  = " HeaderExists == \"x-no-cache\""
  enabled = "true"
}
