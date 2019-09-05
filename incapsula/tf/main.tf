# configure the site

resource "incapsula_site" "site" {
  account_id             = "${var.account_id}"
  domain                 = "secure.${var.domain_name}"
  send_site_setup_emails = "true"
  site_ip                = "35.43.45.6"
  force_ssl              = "true"
  log_level              = "full"
}

resource "incapsula_data_center" "dc1" {
  name           = "forwarding_dc"
  site_id        = "${incapsula_site.site.id}"
  server_address = "${var.site_ip}"
  is_content     = "true"
}

## Security Rule: Blacklist IP
#resource "incapsula_acl_security_rule" "blacklist" {
#  rule_id = "api.acl.blacklisted_ips"
#  site_id = "${incapsula_site.site.id}"
#  ips     = ["0.0.0.0/0"]
#}

#resource "incapsula_acl_whitelist_rule" "url-whitelist" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_acl_security_rule.blacklist.rule_id}"
#  urls              = ["/cds-au/v1/banking/products", "/cds-au/v1/banking/products/$${ID}"]
#  countries         = ["AU"]
#  exception_id_only = "true"
#}

#resource "incapsula_acl_whitelist_rule" "ip-whitelist" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_acl_security_rule.blacklist.rule_id}"
#  urls = ["/foo","/bar"]
#  ips               = ["202.1.23.2", "201.3.45.6", "10.0.0.1"]
#  exception_id_only = "true"
#}

#resource "incapsula_acl_security_rule" "url" {
#  site_id      = "${incapsula_site.site.id}"
#  rule_id      = "api.acl.blacklisted_urls"
#  urls         = ["/ "]
#  url_patterns = ["PREFIX"]
#}

#resource "incapsula_acl_whitelist_rule" "whitelist-url" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_acl_security_rule.url.rule_id}"
#  urls              = ["/bravo", "/bravo/$${ID}", "/thisalso"]
#  exception_id_only = "true"
#}

#resource "incapsula_acl_security_rule" "countries" {
# rule_id   = "api.acl.blacklisted_countries"
# site_id   = "${incapsula_site.site.id}"
# countries = ["DE", "US"]
#
# #  depends_on = [
# #    "incapsula_acl_security_rule.continents"]
#}
#
#resource "incapsula_acl_whitelist_rule" "countries-whitelist" {
# site_id           = "${incapsula_site.site.id}"
# rule_id           = "${incapsula_acl_security_rule.countries.rule_id}"
# countries         = ["AU", "PH"]
# exception_id_only = "true"
#}

#
## Security Rule: Whitelist IP
## This resource can only be used once in a module - there is a race condition if we added multiple resource
#resource "incapsula_acl_security_rule" "whitelist" {
#  rule_id    = "api.acl.whitelisted_ips"
#  site_id    = "${incapsula_site.site.id}"
#  ips        = ["1.136.104.203/32", "10.32.34.5/32", "102.32.45.55/32"]
#  depends_on = ["incapsula_acl_security_rule.blacklist"]
#}
#
## Block certain countries based on country code
#resource "incapsula_acl_security_rule" "continents" {
#  rule_id = "api.acl.blacklisted_countries"
#  site_id = "${incapsula_site.site.id}"
#  continents = ["AS","AF","EU","SA","NA"]
##  countries = ["UA"]
##  depends_on = ["incapsula_acl_security_rule.blacklist",
#    "incapsula_acl_security_rule.whitelist"]
#}

#resource "incapsula_acl_security_rule" "url" {
#  rule_id = "api.acl.blacklisted_urls"
#  site_id = "${incapsula_site.site.id}"
#  url_patterns = "EQUALS,EQUALS"
#  urls = "/alpha,/bravo"
#  depends_on = ["incapsula_site.site", "incapsula_acl_security_rule.countries"]
#}
#
## Incap Rule: Rewrite Header (ADR)
#resource "incapsula_incap_rule" "rewrite-header" {
#  priority      = "17"
#  name          = "change_host_header"
#  site_id       = "${incapsula_site.site.id}"
#  action        = "RULE_ACTION_REWRITE_HEADER"
#  add_missing   = "true"
#  from          = "gcpnp.api-np.anz"
#  to            = "api-np.api.sec.gcpnp.anz"
#  allow_caching = "false"
#  rewrite_name  = "Host"
#}
#
#resource "incapsula_incap_certificate" "ssl" {
#  site_id     = "${incapsula_site.site.id}"
#  certificate = "${base64encode(file(var.certificate))}"
#  private_key = "${base64encode(file(var.private_key))}"
#}
#
#resource "incapsula_incap_rule" "redirect" {
#  name = "redirect_to_https"
#  site_id = "${incapsula_site.site.id}"
#  action = "RULE_ACTION_REDIRECT"
#  priority = "18"
#  response_code = "301"
#  from = "http://www.mydomain.com"
#  to = "https://www.mydomain.com"
#}
#
## Block request if custom header does not exist#
#resource "incapsula_incap_rule" "magic-header" {
#  name          = "block_without_magic_header"
#  site_id       = "${incapsula_site.site.id}"
#  action        = "RULE_ACTION_REDIRECT"
#  priority      = "19"
#  filter        = "HeaderExists != \"anz-magic-token\" & HeaderValue != {\"anz-magic-token\";\"bc339c8d57843580d0020e95778aa22e503a581cf82679e6c76f168544de3b20\"}"
#  response_code = "301"
#  from          = "https://mydomain.com"
#  to            = "https://errorpage.com"
#}

#resource "incapsula_incap_rule" "magic-header" {
#  name     = "block_without_magic_header"
#  site_id  = "${incapsula_site.site.id}"
##  action   = "RULE_ACTION_BLOCK"
#  priority = "19"
#  filter   = "HeaderValue != {\"anz-magic-token\";\"bc339c8d57843580d0020e95778aa22e503a581cf82679e6c76f168544de3b20\"}"
#}

#resource "incapsula_incap_rule" "rewrite-istio-header" {
#  name          = "rewrite_server_to_anz"
#  site_id       = "${incapsula_site.site.id}"
#  action        = "RULE_ACTION_REWRITE_HEADER"
#  priority      = "20"
#  rewrite_name  = "server"
#  from          = "istio-envoy"
#  to            = "anz"
#}
#
##resource "incapsula_cache_rule" "cache1" {
##  site_id = "${incapsula_site.site.id}"
##  name = "x-min-v_cache_key"
##  action = "HTTP_CACHE_DIFFERENTIATE_BY_HEADER"
##  filter = "HeaderExists == \"x-min-v\""
##  differentiated_by_value = "x-min-v"
##}
#
#resource "incapsula_cache_rule" "cache2" {
#  name = "force_this_cache"
#  site_id = "${incapsula_site.site.id}"
#  action = "HTTP_CACHE_FORCE_UNCACHEABLE"
#}

#resource "incapsula_cache_rule" "cache3" {
#  name = "enrich_cache"
#  site_id = "${incapsula_site.site.id}"
#  action = "HTTP_CACHE_IGNORE_PARAMS"
#  params = "param1"
#}
#
## Update the WAF security rule (sql injection)
## Raise condition on API - if the same resource need to specifically define depends_on attribute
#resource "incapsula_waf_security" "waf1" {
#  site_id              = "${incapsula_site.site.id}"
#  rule_id              = "api.threats.sql_injection"
#  security_rule_action = "api.threats.action.block_request"
#}
#
### SQL injection whitelist
#resource "incapsula_acl_whitelist_rule" "sql-whitelist" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_waf_security.waf1.rule_id}"
#  ips               = ["100.0.0.1", "200.0.0.1", "10.0.0.1"]
#  exception_id_only = "true"
#}
#
### Cross site scripting threat
#resource "incapsula_waf_security" "waf2" {
#  site_id              = "${incapsula_site.site.id}"
#  rule_id              = "api.threats.cross_site_scripting"
#  security_rule_action = "api.threats.action.block_request"
#
#  depends_on = [
#    "incapsula_waf_security.waf1",
#  ]
#}
#
### Cross site scripting whitelist
#resource "incapsula_acl_whitelist_rule" "xxs-whitelist" {
#  site_id           = "${incapsula_site.site.id}"
#  rule_id           = "${incapsula_waf_security.waf2.rule_id}"
#  ips               = ["8.8.8.8", "4.4.4.4", "8.8.4.4"]
#  urls              = ["/bravo"]
#  client_apps       = ["488","133"]
#  parameters        = ["qwerty","cache"]
##  countries         = ["US","AU"]
#  exception_id_only = "true"
#}

#
## Backdoor protect
#resource "incapsula_waf_security" "waf4" {
#  site_id = "${incapsula_site.site.id}"
#  rule_id = "api.threats.backdoor"
#  security_rule_action = "api.threats.action.alert"
#  depends_on = ["incapsula_waf_security.waf1",
#    "incapsula_waf_security.waf2"]
#}
#
#resource "incapsula_waf_security" "waf5" {
#  site_id = "${incapsula_site.site.id}"
#  rule_id = "api.threats.illegal_resource_access"
#  security_rule_action = "api.threats.action.alert"
#  depends_on = ["incapsula_waf_security.waf1",
#    "incapsula_waf_security.waf2",
#    "incapsula_waf_security.waf4"]
#}
#
#resource "incapsula_waf_security" "waf6" {
#  site_id = "${incapsula_site.site.id}"
#  rule_id = "api.threats.bot_access_control"
#  block_bad_bots = "true"
#  challenge_suspected_bots = "true"
#  depends_on = ["incapsula_waf_security.waf1",
#    "incapsula_waf_security.waf2",
#    "incapsula_waf_security.waf4",
#    "incapsula_waf_security.waf5"]
#}
#
#resource "incapsula_waf_security" "ddos" {
#  site_id = "${incapsula_site.site.id}"
# rule_id = "api.threats.ddos"
#  activation_mode = "api.threats.ddos.activation_mode.auto"
#  ddos_traffic_threshold = "500"
#  depends_on = ["incapsula_waf_security.waf1",
#    "incapsula_waf_security.waf2"]
#    "incapsula_waf_security.waf4",
#    "incapsula_waf_security.waf5",
#    "incapsula_waf_security.waf6"]
#}

# Example cache response header

#resource "incapsula_cache_response_headers" "cacheheaders" {
#  site_id       = "${incapsula_site.site.id}"
#  cache_headers = ["server", "x-v"]
#}
#
#resource "incapsula_cache_mode" "cacheMode" {
#  site_id                = "${incapsula_site.site.id}"
#  cache_mode             = "static_and_dynamic"
#  dynamic_cache_duration = "60_min"
#}
#
#resource "incapsula_data_storage_region" "dataStorage" {
#  site_id             = "${incapsula_site.site.id}"
#  data_storage_region = "APAC"
#}
# This will redirect all request from http to https
resource "incapsula_incap_rule" "redirect" {
  name          = "redirect_site_to_https"
  enabled       = false
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REDIRECT"
  priority      = "1"
  response_code = "301"
  from          = "http://secure.api.${var.domain_name}/*"
  to            = "https://secure.api.${var.domain_name}/$1"
}

resource "incapsula_incap_rule" "redirect-to-support" {
  name          = "base_page_redirect_to_support_site"
  enabled       = false
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REDIRECT"
  priority      = "2"
  response_code = "301"
  filter        = "URL == \"/\""
  to            = "https://www.anz.com.au/support/anz-apis/"
}

# redirect http and https://www.api.anz call to https://www.anz.com.au/support/anz-apis/ (GCP-240)
resource "incapsula_incap_rule" "redirect_http_www" {
  name          = "redirect_http_www_to_support"
  enabled       = true
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REDIRECT"
  priority      = "3"
  response_code = "301"
  from          = "http://secure.api.${var.domain_name}/*"
  to            = "https://www.anz.com.au/support/anz-apis/"
}

resource "incapsula_incap_rule" "forward-to-dc" {
  name     = "client_ssl_forward"
  enabled  = "true"
  site_id  = "${incapsula_site.site.id}"
  action   = "RULE_ACTION_FORWARD_TO_DC"
  filter   = "ClientCertExist == Yes  & URL contains \"^/app\""
  priority = "99"
  dc_id    = "${incapsula_data_center.dc1.id}"
}

#resource "incapsula_incap_rule" "redirect_https_www" {
#  name          = "redirect_https_www_to_support"
#  enabled       = true
#  site_id       = "${incapsula_site.site.id}"
#  action        = "RULE_ACTION_REDIRECT"
#  priority      = "4"
#  response_code = "301"
#  from          = "https://secure.api.${var.domain_name}/*"
#  to            = "https://www.anz.com.au/support/anz-apis/"
#}

