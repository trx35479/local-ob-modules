# configure the site

resource "incapsula_site" "site" {
  domain                 = "${var.domain_name}"
  account_id             = "1284650"
  send_site_setup_emails = "true"
  site_ip                = "35.244.110.71"
  force_ssl              = "true"
  log_level              = "full"
}

# Security Rule: Blacklist IP
resource "incapsula_acl_security_rule" "blacklist" {
  rule_id    = "api.acl.blacklisted_ips"
  site_id    = "${incapsula_site.site.id}"
  ips        = "${var.blacklist_ips}"
  depends_on = ["incapsula_site.site"]
}

# Security Rule: Whitelist IP
# This resource can only be used once in a module - there is a race condition if we added multiple resource
resource "incapsula_acl_security_rule" "whitelist" {
  rule_id    = "api.acl.whitelisted_ips"
  site_id    = "${incapsula_site.site.id}"
  ips        = "${var.whitelist_ips}"
  depends_on = ["incapsula_site.site", "incapsula_acl_security_rule.blacklist"]
}

# Incap Rule: Rewrite Header (ADR)
resource "incapsula_incap_rule" "rewrite-header" {
  priority      = "17"
  name          = "change_host_header"
  site_id       = "${incapsula_site.site.id}"
  action        = "RULE_ACTION_REWRITE_HEADER"
#  add_missing   = "true"
  from          = "${var.rewrite_from}"
  to            = "${var.rewrite_to}"
  allow_caching = "false"
  rewrite_name  = "${var.rewrite_name}"
  depends_on    = ["incapsula_site.site"]
}