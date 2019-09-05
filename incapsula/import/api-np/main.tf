// import to state file

//import site
terraform import module.public-infra.incapsula_site.site 55045384

//import rules
terraform import module.public-infra.incapsula_incap_rule.rewrite-header 55045384/188520

//import whitelist
terraform import module.public-infra.incapsula_acl_security_rule.whitelist 55045384/api.acl.whitelisted_ips

//import blacklist
terraform import module.public-infra.incapsula_acl_security_rule.blacklist 55045384/api.acl.blacklisted_ips

