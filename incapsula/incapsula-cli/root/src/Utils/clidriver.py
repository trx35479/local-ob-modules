import argparse
from Accounts.cAccount import c_account
from Accounts.rAudit import r_audit
from Sites.cSite import c_site
from Sites.dCertificate import d_certificate
from Sites.dSite import d_site
from Sites.rSite import r_site
from Sites.rSites import r_sites
from Sites.uACL import u_acl
from Sites.uCacheMode import u_cachemode
from Sites.uAdvanced import u_advanced
from Sites.uCachingRules import u_cacherule
from Sites.uCertificate import u_certificate
from Sites.uConfigration import u_configuration
from Sites.uWaf import u_security
from Sites.uWhitelist import u_whitelist
from Sites.cIncapRule import c_incaprule
from Sites.rIncapRule import r_incaprule
from Sites.uIncapRule import u_incaprule
from Sites.dIncapRule import d_incaprule
from Config.configuration import configure
from Utils.cSite_restore import c_site_restore
from Accounts.rAccounts import r_accounts
from Accounts.rAccount import r_account
from Accounts.rSubAccounts import r_subaccount
from _version import __version__


parser = argparse.ArgumentParser(prog='incap',
                                 usage='%(prog)s <resource> <command> [options]',
                                 description="CLI for site, account and security CRUD on Incapsula via API.")
parser.add_argument('--version', action='version', version=__version__)
subparsers = parser.add_subparsers()

cli_config_parser = subparsers.add_parser('config', help='Use config to add the default API_ID,'
                                                         ' API_KEY and Account_ID.',
                                          usage='incap config [options] api_id api_key account_id')
cli_config_parser.add_argument('api_id', help='API authentication identifier.')
cli_config_parser.add_argument('api_key', help='API authentication identifier.')
cli_config_parser.add_argument('account_id', help='Numeric identifier of the account to operate'
                                                  ' on. If not specified, operation will be '
                                                  'performed on the account identified by the '
                                                  'authentication parameters.')
cli_config_parser.add_argument('--repo', default='', help='This is optional if you have a '
                                                            'repository where backups and templates can be storied.')
cli_config_parser.add_argument('--baseurl', default='https://my.incapsula.com',
                               help='Optionally set the URL for the API domain.')
cli_config_parser.add_argument('--log', default='INFO')
cli_config_parser.set_defaults(func=configure)

# cli_archive_parser = subparsers.add_parser('archive', help='Use config to add the default API_ID,'
#                                                            ' API_KEY and Account_ID.',
#                                            usage='incap config [options] api_id api_key account_id')
# cli_archive_parser.add_argument('api_id', help='API authentication identifier.')
# cli_archive_parser.add_argument('api_key', help='API authentication identifier.')
# cli_archive_parser.add_argument('account_id', help='Numeric identifier of the account to operate'
#                                                   ' on. If not specified, operation will be '
#                                                   'performed on the account identified by the '
#                                                   'authentication parameters.')
# cli_archive_parser.add_argument('--baseUrl', default='https://my.incapsula.com')
# cli_archive_parser.add_argument('--log', default='INFO')
# cli_archive_parser.set_defaults(func=create_repo)

site_parser = subparsers.add_parser('site', help='Used to add, delete and configure Incapsula sites.',
                                    usage='incap site <command> [options]')
site_subparsers = site_parser.add_subparsers()
site_add_parser = site_subparsers.add_parser('add',
                                             help='Add a new site to an account. '
                                                  'If the site already exists, its status is returned.',
                                             usage='incap site add [options] domain')
site_add_parser.add_argument('--api_id', help='API authentication identifier.')
site_add_parser.add_argument('--api_key', help='API authentication identifier.')
site_add_parser.add_argument('--account_id',
                             help='Numeric identifier of the account to operate on. '
                                  'If not specified, operation will be performed on the account '
                                  'identified by the authentication parameters.')

site_add_parser.add_argument('--ref_id', default='',
                             help='Customer specific identifier for this operation.')
site_add_parser.add_argument('--send_site_setup_emails', default='',
                             help='If this value is "false", end users will not get emails about the add site process '
                                  'such as "DNS instructions" and "SSL setup".')
site_add_parser.add_argument('--site_ip', default='',
                             help='Manually set the web server IP/CNAME. This option is only available '
                                  'for specific accounts.')
site_add_parser.add_argument('--force_ssl', default='',
                             help='If this value is "true", manually set the site to support SSL. '
                                  'This option is only available for sites with manually configured IP/CNAME and '
                                  'for specific accounts.')
site_add_parser.add_argument('--log_level', default='',
                             help='Available only for Enterprise Plan customers that purchased the '
                                  'Logs Integration SKU. Sets the log reporting level for the site. Options'
                                  ' are “full”, “security”, “none” and "default"')
site_add_parser.add_argument('--logs_account_id', default='',
                             help='Available only for Enterprise Plan customers that purchased the '
                                  'Logs Integration SKU. Numeric identifier of the account that purchased the logs'
                                  ' integration SKU and which collects the logs. If not specified, operation will '
                                  'be performed on the account identified by the authentication parameters')
site_add_parser.add_argument('domain', help='The domain name of the site. '
                                            'For example: www.example.com, hello.example.com, example.com')
site_add_parser.add_argument('--log', default='INFO')
site_add_parser.set_defaults(func=c_site)

site_restore_parser = site_subparsers.add_parser('restore', help='Use this operation to bulk add sites.',
                                                 usage='incap site restore [options] path')
site_restore_parser.add_argument('--api_id', help='API authentication identifier.')
site_restore_parser.add_argument('--api_key', help='API authentication identifier.')
site_restore_parser.add_argument('--account_id',
                                 help='Numeric identifier of the account to operate on. '
                                      'If not specified, operation will be performed on the account '
                                      'identified by the authentication parameters.')
site_restore_parser.add_argument('--domain', default=None, help='The new domain/site you would like to add.')
site_restore_parser.add_argument('path', help='The file or directory with multiple files.')
site_restore_parser.add_argument('--log', default='INFO')
site_restore_parser.set_defaults(func=c_site_restore)

site_delete_parser = site_subparsers.add_parser('delete', help='Use this operation to delete a site.',
                                                usage='incap site delete [options] site_id')
site_delete_parser.add_argument('--api_id', help='API authentication identifier.')
site_delete_parser.add_argument('--api_key', help='API authentication identifier.')
site_delete_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_delete_parser.add_argument('--log', default='INFO')
site_delete_parser.set_defaults(func=d_site)

site_status_parser = site_subparsers.add_parser('status', help='Use this operation to get the status of a site.',
                                                usage='incap site status [options] site_id')
site_status_parser.add_argument('--api_id', help='API authentication identifier.')
site_status_parser.add_argument('--api_key', help='API authentication identifier.')
site_status_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_status_parser.add_argument('--tests', default='', help='List of tests to run on site before returning its status. '
                                                            'A comma separated list of one of: '
                                                            'domain_validation, services, dns. '
                                                            'See detailed description below.')
site_status_parser.add_argument('--log', default='INFO')
site_status_parser.set_defaults(func=r_site)

site_ucertificate_parser = site_subparsers.add_parser('upcert', help='Use this operation to upload custom '
                                                                    'certificate for your site. The following SSL '
                                                                    'certificate file formats are supported:'
                                                                    ' PFX, PEM, CER.',
                                                     usage='incap site upcert [options] certificate site_id')
site_ucertificate_parser.add_argument('--api_id', help='API authentication identifier.')
site_ucertificate_parser.add_argument('--api_key', help='API authentication identifier.')
site_ucertificate_parser.add_argument('certificate', help='The certificate file in base64 format (location)')
site_ucertificate_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_ucertificate_parser.add_argument('--private_key', help='The private key of the certificate in base64 format.'
                                                           ' Optional in case of PFX certificate file format')
site_ucertificate_parser.add_argument('--passphrase', help='The passphrase used to protect your SSL certificate')
site_ucertificate_parser.add_argument('--log', default='INFO')
site_ucertificate_parser.set_defaults(func=u_certificate)

site_dcertificate_parser = site_subparsers.add_parser('delcert', help='Use this operation to upload custom '
                                                                    'certificate for your site. The following SSL '
                                                                    'certificate file formats are supported:'
                                                                    ' PFX, PEM, CER.',
                                                     usage='incap site upcert [options] certificate site_id')
site_dcertificate_parser.add_argument('--api_id', help='API authentication identifier.')
site_dcertificate_parser.add_argument('--api_key', help='API authentication identifier.')
site_dcertificate_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_dcertificate_parser.add_argument('--log', default='INFO')
site_dcertificate_parser.set_defaults(func=d_certificate)

site_list_parser = site_subparsers.add_parser('list', help='Use this operation to delete a site.',
                                              usage='incap site list [options]')
site_list_parser.add_argument('--api_id', help='API authentication identifier.')
site_list_parser.add_argument('--api_key', help='API authentication identifier.')
site_list_parser.add_argument('--account_id',
                              help='Numeric identifier of the account to operate on. If not specified, '
                                   'operation will be performed on the account identified '
                                   'by the authentication parameters.')
site_list_parser.add_argument('--page_size',
                              help='The number of objects to return in the response. Default is 50.')
site_list_parser.add_argument('--page_num', help='The page to return starting from 0, Default is 0.')
site_list_parser.add_argument('--export', default=False, help='Set to true to export files locally.')
site_list_parser.add_argument('--path', default=None, help='If export is selected, you can specify the '
                                                           'FULL path; default is current dir OR'
                                                           ' the path configured in the config.ini.')
site_list_parser.add_argument('--filename', default="{site_id}_{domain}_{date}",
                              help='If export is selected, you can specify the file name.'
                                   'Default name is {site_id}_{domain}_{date}.\r'
                                   'Optional files name:\r'
                                   '{site_id}_{domain}\r'
                                   '{site_id}\r'
                                   '{domain}\r'
                                   '{site_id}_{domain}_CUSTOM -- Ex: {site_id}_{domain}_Rev3_0B')
site_list_parser.add_argument('--log', default='INFO')
site_list_parser.set_defaults(func=r_sites)

site_configure_parser = site_subparsers.add_parser('configure',
                                                   help='Use this operation to change one of the basic '
                                                        'configuration settings of the site.',
                                                   usage='incap site configure [options] param value site_id')
site_configure_parser.add_argument('--api_id', help='API authentication identifier.')
site_configure_parser.add_argument('--api_key', help='API authentication identifier.')
site_configure_parser.add_argument('param', help='According to the param value, see table below.')
site_configure_parser.add_argument('value', help='Name of configuration parameter to set.')
site_configure_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_configure_parser.add_argument('--log', default='INFO')
site_configure_parser.set_defaults(func=u_configuration)

site_security_parser = site_subparsers.add_parser('security',
                                                  help='Use this operation to change the security '
                                                       'configuration of a site. To modify the configuration for '
                                                       'a specific rule, additional parameters may be required, as '
                                                       'documented below.',
                                                  usage='incap site security [options] rule_id site_id')
site_security_parser.add_argument('--api_id', help='API authentication identifier.')
site_security_parser.add_argument('--api_key', help='API authentication identifier.')
site_security_parser.add_argument('rule_id', help='ID of the security rule to change. \nFor possible values,'
                                                  ' see the security section in the Get site status API call.\n'
                                                  'bot_access_control, sql_injection, cross_site_scripting,'
                                                  'illegal_resource_access, ddos, or backdoor.')
site_security_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_security_parser.add_argument('--block_bad_bots', '--block_bad_bots=< true,false>', default='',
                                  help='Whether or not to block bad bots. Possible values: true, false')
site_security_parser.add_argument('--challenge_suspected_bots', '--challenge_suspected_bots=<true,false>', default='',
                                  help='Whether or not to send a challenge to clients that are '
                                       'suspected to be bad bots (CAPTCHA for example). Possible values: true, false')
site_security_parser.add_argument('--activation_mode', default='',
                                  help='DDOS activiation mode - For example, for "off", use '
                                       'activation_mode=off.')
site_security_parser.add_argument('--security_rule_action', default='',
                                  help='The action that should be taken when a threat is detected, '
                                       'for example: block_ip, disabled, alert, block_user, block_ip, quarantine_url. '
                                       'Different actions are allowed per different threats,'
                                       ' e.g. backdoors may only be quarantined, ignored, or trigger an alert.'
                                       ' For possible values see the security_rule_action table below.')
site_security_parser.add_argument('--quarantined_urls', default='',
                                  help='A comma separated list of encoded URLs to be kept in quarantine. '
                                       '--quarantined_urls=<str>')
site_security_parser.add_argument('--ddos_traffic_threshold', default='',
                                  help='Consider site to be under DDoS if the request rate is above this threshold. '
                                       'The valid values are 10, 20, 50, 100, 200, '
                                       '500, 750, 1000, 2000, 3000, 4000, 5000. i.e. --ddos_traffic_threshold=<10')
site_security_parser.add_argument('--log', default='INFO')
site_security_parser.set_defaults(func=u_security)

site_acl_parser = site_subparsers.add_parser('acl', help='Use this operation to change ACL configuration of a site.\n'
                                                         'To modify the configuration for a specific ACL rule, '
                                                         'its values are required, as documented below.\n'
                                                         'string as the list values.',
                                             usage='incap site acl [options] rule_id site_id')
site_acl_parser.add_argument('--api_id', help='API authentication identifier.')
site_acl_parser.add_argument('--api_key', help='API authentication identifier.')
site_acl_parser.add_argument('rule_id', help='The id of the acl, e.g blacklisted_ips, blacklisted_countries,'
                                             ' blacklisted_urls, blacklisted_ips, whitelisted_ips')
site_acl_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_acl_parser.add_argument('--urls', default='',
                             help='A comma separated list of resource paths. Yes For example,'
                                  ' /home and /admin/index.html are resource paths, however http://www.example.com/home'
                                  ' is not. Each URL should be encoded separately using percent encoding as '
                                  'specified by RFC 3986 (http://tools.ietf.org/html/rfc3986#section- 2.1). '
                                  'An empty URL list will remove all URLs.')
site_acl_parser.add_argument('--url_patterns', default=None,
                             help='A comma separated list of url patterns, one Yes of: '
                                  'contains | equals | prefix | suffix | not_equals | not_contain | '
                                  'not_prefix | not_suffix. The patterns should be in accordance with the '
                                  'matching urls sent by the urls parameter.')
site_acl_parser.add_argument('--countries', default='', help='A comma separated list of country codes')
site_acl_parser.add_argument('--continents', default='', help='A comma separated list of continent codes')
site_acl_parser.add_argument('--ips', default='', help='A comma separated list of IPs or IP ranges, '
                                                       'e.g: 192.168.1.1, 192.168.1.1- 192.168.1.100 or 192.168.1.1/24')
site_acl_parser.add_argument('--log', default='INFO')
site_acl_parser.set_defaults(func=u_acl)

site_add_incaprule_parser = site_subparsers.add_parser('add_incaprule',
                                                       help='Use this operation to add a '
                                                            'rule (Delivery Rules or IncapRules).',
                                                            usage='incap site incaprule [options] site_id')
site_add_incaprule_parser.add_argument('--api_id', help='API authentication identifier.')
site_add_incaprule_parser.add_argument('--api_key', help='API authentication identifier.')
site_add_incaprule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_add_incaprule_parser.add_argument('--name', default='', help='Rule Name')
site_add_incaprule_parser.add_argument('--action', default='',
                                       help='Rule action. See the possible values in the table below.')
site_add_incaprule_parser.add_argument('--filter', default='',
                                       help='Rule will trigger only a request that matches this filter. '
                                            'For more details on filter guidelines, see Syntax Guide.')
site_add_incaprule_parser.add_argument('--response_code', default='',
                                       help="Redirect rule's response code. Valid values are 302, 301, 303, 307, 308.")
site_add_incaprule_parser.add_argument('--protocol', default='',
                                       help='')
site_add_incaprule_parser.add_argument('--add_missing', default='',
                                       help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
site_add_incaprule_parser.add_argument('--from', dest='origin', default='',
                                       help='The pattern to rewrite. '
                                            'RULE_ACTION_REWRITE_URL - The URL to rewrite. '
                                            'RULE_ACTION_REWRITE_HEADER - The header value to rewrite. '
                                            'RULE_ACTION_REWRITE_COOKIE - The cookie value to rewrite.')
site_add_incaprule_parser.add_argument('--to', default='',
                                       help='The pattern to change to. '
                                            'RULE_ACTION_REWRITE_URL - The URL to change to.'
                                            ' RULE_ACTION_REWRITE_HEADER - The header value to change to. '
                                            'RULE_ACTION_REWRITE_COOKIE - The cookie value to change to.')
site_add_incaprule_parser.add_argument('--rewrite_name', default='',
                                       help='Name of cookie or header to rewrite. '
                                            'Applies only for RULE_ACTION_REWRITE_COOKIE '
                                            'and RULE_ACTION_REWRITE_HEADER.')
site_add_incaprule_parser.add_argument('--dc_id', default='',
                                       help='Data center to forward request to. '
                                            'Applies only for RULE_ACTION_FORWARD_TO_DC.')
site_add_incaprule_parser.add_argument('--is_test_mode', default='',
                                       help='Make rule apply only for IP address the API request was sent from.')
site_add_incaprule_parser.add_argument('--lb_algorithm', default='',
                                       help='Data center load balancing algorithm. Possible values are: '
                                            'LB_LEAST_PENDING_REQUESTS - Server with least pending requests '
                                            'LB_LEAST_OPEN_CONNECTIONS - Server with least open connections '
                                            'LB_SOURCE_IP_HASH - Server by IP hash RANDOM - Random server')
site_add_incaprule_parser.add_argument('--log', default='INFO')
site_add_incaprule_parser.set_defaults(func=c_incaprule)

site_edit_incaprule_parser = site_subparsers.add_parser('edit_incaprule',
                                                        help='Use this operation to edit an existing '
                                                        'rule (Delivery Rules or IncapRules).',
                                                        usage='incap site edit_incaprule [options] rule_id')
site_edit_incaprule_parser.add_argument('--api_id', help='API authentication identifier.')
site_edit_incaprule_parser.add_argument('--api_key', help='API authentication identifier.')
site_edit_incaprule_parser.add_argument('rule_id', help='Rule ID.')
site_edit_incaprule_parser.add_argument('--name', default='', help='Rule Name')
site_edit_incaprule_parser.add_argument('--action', default='',
                                        help='Rule action. See the possible values in the table below.')
site_edit_incaprule_parser.add_argument('--filter', default='',
                                        help='Rule will trigger only a request that matches this filter. '
                                        'For more details on filter guidelines, see Syntax Guide.')
site_edit_incaprule_parser.add_argument('--response_code', default='',
                                        help='')
site_edit_incaprule_parser.add_argument('--protocol', default='',
                                        help='')
site_edit_incaprule_parser.add_argument('--add_missing', default='',
                                        help="Add cookie or header if it doesn't exist (Rewrite cookie rule only)")
site_edit_incaprule_parser.add_argument('--from', dest='origin', default='',
                                        help='The pattern to rewrite. '
                                             'RULE_ACTION_REWRITE_URL - The URL to rewrite. '
                                             'RULE_ACTION_REWRITE_HEADER - The header value to rewrite. '
                                             'RULE_ACTION_REWRITE_COOKIE - The cookie value to rewrite.')
site_edit_incaprule_parser.add_argument('--to', default='',
                                        help='The pattern to change to. '
                                             'RULE_ACTION_REWRITE_URL - The URL to change to. '
                                             'RULE_ACTION_REWRITE_HEADER - The header value to change to. '
                                             'RULE_ACTION_REWRITE_COOKIE - The cookie value to change to.')
site_edit_incaprule_parser.add_argument('--rewrite_name', default='',
                                        help='Name of cookie or header to rewrite. '
                                             'Applies only for RULE_ACTION_REWRITE_COOKIE '
                                             'and RULE_ACTION_REWRITE_HEADER.')
site_edit_incaprule_parser.add_argument('--dc_id', default='',
                                        help='Data center to forward request to. '
                                             'Applies only for RULE_ACTION_FORWARD_TO_DC.')
site_edit_incaprule_parser.add_argument('--is_test_mode', default='',
                                        help='Make rule apply only for IP address the API request was sent from.')
site_edit_incaprule_parser.add_argument('--lb_algorithm', default='',
                                        help='Data center load balancing algorithm. Possible values are:'
                                        ' LB_LEAST_PENDING_REQUESTS - Server with least pending requests'
                                        ' LB_LEAST_OPEN_CONNECTIONS - Server with least open connections'
                                        ' LB_SOURCE_IP_HASH - Server by IP hash'
                                        ' RANDOM - Random server')
site_edit_incaprule_parser.add_argument('--log', default='INFO')
site_edit_incaprule_parser.set_defaults(func=u_incaprule)

site_delete_incaprule_parser = site_subparsers.add_parser('del_incaprule', help='Use this operation to delete a '
                                                                                'rule (Delivery Rules or IncapRules).',
                                                          usage='incap site delete_incaprule [options] rule_id')
site_delete_incaprule_parser.add_argument('--api_id', help='API authentication identifier.')
site_delete_incaprule_parser.add_argument('--api_key', help='API authentication identifier.')
site_delete_incaprule_parser.add_argument('rule_id', help='Numeric identifier of the site to operate on.')
site_delete_incaprule_parser.add_argument('--log', default='INFO')
site_delete_incaprule_parser.set_defaults(func=d_incaprule)

site_list_incaprule_parser = site_subparsers.add_parser('list_incaprule',
                                                        help='Use this operation to list rules '
                                                             '(Delivery Rules and IncapRules) for a given site.',
                                                        usage='incap site list_incaprule [options] site_id')
site_list_incaprule_parser.add_argument('--api_id', help='API authentication identifier.')
site_list_incaprule_parser.add_argument('--api_key', help='API authentication identifier.')
site_list_incaprule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_list_incaprule_parser.add_argument('--include_ad_rules', default='',
                                        help='Whether or not delivery rules should be included. Defaults to "Yes".')
site_list_incaprule_parser.add_argument('--include_incap_rules', default='',
                                        help='Whether or not security rules be included. Defaults to "Yes".')
site_list_incaprule_parser.add_argument('--page_size', default='',
                                        help='The number of objects to return in the response. Default is 50.')
site_list_incaprule_parser.add_argument('--page_num', default='',
                                        help='The page to return starting from 0. Default is 0.')
site_list_incaprule_parser.add_argument('--log', default='INFO')
site_list_incaprule_parser.set_defaults(func=r_incaprule)

site_whitelist_parser = site_subparsers.add_parser('whitelist', help='Use this operation to set whitelists '
                                                                     'to security rules or ACLs. '
                                                                     'To update an existing whitelist, '
                                                                     'send its ID in the id parameter. '
                                                                     'If the id parameter does not exist a '
                                                                     'new whitelist will be created.',
                                                   usage='incap site whitelist [options] rule_id site_id')
site_whitelist_parser.add_argument('--api_id', help='API authentication identifier.')
site_whitelist_parser.add_argument('--api_key', help='API authentication identifier.')
site_whitelist_parser.add_argument('rule_id', help='ID of the security rule to change. '
                                                   'For possible values, see the security section in the '
                                                   'Get site status API call. [api.threats.bot_access_control,'
                                                   'api.threats.sql_injection,api.threats.cross_site_scripting'
                                                   ',api.threats.illegal_resource_access,api.threats.ddos,'
                                                   'api.threats.backdoor]')
site_whitelist_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_whitelist_parser.add_argument('--whitelist_id', default='', help='The id (an integer) of the whitelist to be set. '
                                                                      'This field is optional - '
                                                                      'in case no id is supplied, a new whitelist will '
                                                                      'be created.')
site_whitelist_parser.add_argument('--delete_whitelist', default='',
                                   help='An optional boolean parameter, in case it is set to "true" '
                                        'and a whitelist id is sent, then the whitelist will be deleted.')
site_whitelist_parser.add_argument('--urls', default='',
                                   help='A comma separated list of resource paths. '
                                        'Yes For example, /home and /admin/index.html are resource paths, '
                                        'however http://www.example.com/home is not. '
                                        'Each URL should be encoded separately using percent encoding as '
                                        'specified by RFC 3986 (http://tools.ietf.org/html/rfc3986#section- 2.1).'
                                        ' An empty URL list will remove all URLs.')
site_whitelist_parser.add_argument('--countries', default='', help='A comma separated list of country codes')
site_whitelist_parser.add_argument('--continents', default='', help='A comma separated list of continent codes')
site_whitelist_parser.add_argument('--ips', default='', help='A comma separated list of IPs or IP ranges,'
                                                             ' e.g: 192.168.1.1, 192.168.1.1- 192.168.1.100 '
                                                             'or 192.168.1.1/24')
site_whitelist_parser.add_argument('--client_app_types', default='',
                                   help='A comma separated list of client application types.')
site_whitelist_parser.add_argument('--client_apps', default='', help='Comma separated list of client application ids.')
site_whitelist_parser.add_argument('--parameters', default='', help='Comma separated list of encoded parameters.')
site_whitelist_parser.add_argument('--user_agents', default='', help='Comma separated list of encoded user agents.')
site_whitelist_parser.add_argument('--log', default='INFO')
site_whitelist_parser.set_defaults(func=u_whitelist)

site_cache_mode_parser = site_subparsers.add_parser('cache-mode', help='Use this operation to edit basic site '
                                                                       'caching settings.',
                                                    usage='incap site cache [options] cache-mode site_id')
site_cache_mode_parser.add_argument('--api_id', help='API authentication identifier.')
site_cache_mode_parser.add_argument('--api_key', help='API authentication identifier.')
site_cache_mode_parser.add_argument('cache_mode', help='disable | static_only | static_and_dynamic | aggressive : '
                                                       'default Static_Only.')
site_cache_mode_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_cache_mode_parser.add_argument('--dynamic_cache_duration', default='',
                               help="Profile dynamic pages and cache duration, pass number followed by"
                                    " '_' and one of: hr | min | sec | days | weeks: default: 5_min.")
site_cache_mode_parser.add_argument('--aggressive_cache_duration', default='',
                               help="Cache resource duration, pass number followed by"
                                    " '_' and one of: hr | min | sec | days | weeks: default: 1_hr.")
site_cache_mode_parser.add_argument('--log', default='INFO')
site_cache_mode_parser.set_defaults(func=u_cachemode)

site_cache_rule_parser = site_subparsers.add_parser('cache-rule', help='Use this operation to edit basic '
                                                                       'site caching settings.',
                                                    usage='incap site cache [options] cache-rule site_id')
site_cache_rule_parser.add_argument('--api_id', help='API authentication identifier.')
site_cache_rule_parser.add_argument('--api_key', help='API authentication identifier.')
site_cache_rule_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_cache_rule_parser.add_argument('--always_cache_resource_url', default='',
                                    help="Comma separated list of always cache resources url")
site_cache_rule_parser.add_argument('--always_cache_resource_pattern', default='',
                                    help="Comma separated list of always cache resources pattern. "
                                    "One of: contains | equals | prefix | suffix | not_equals | not_contains "
                                    "| not_prefix | not_suffix")
site_cache_rule_parser.add_argument('--always_cache_resource_duration', default='',
                                    help="Duration that resources will be in cache, pass number followed by "
                                    "'_' and one of: hr | min | sec | days | weeks. "
                                    "Either provide a comma separated list of duration expressions, "
                                    "matching the number of always cache rules, "
                                    "or a single duration expression to be used for all always cache rules.")
site_cache_rule_parser.add_argument('--never_cache_resource_url', default='',
                                    help="Comma separated list of never cache resources url.")
site_cache_rule_parser.add_argument('--never_cache_resource_pattern', default='',
                                    help="Comma separated list of never cache resources pattern. "
                                    "One of: contains | equals | prefix | suffix | not_equals "
                                    "| not_contains | not_prefix | not_suffix")
site_cache_rule_parser.add_argument('--cache_headers', default='',
                                    help="Comma separated list of cached headers.")
site_cache_rule_parser.add_argument('--clear_always_cache_rules', default='',
                                    help="An optional boolean parameter. If set to 'true', "
                                         "the site's always cache rules will be cleared.")
site_cache_rule_parser.add_argument('--clear_never_cache_rules', default='',
                                    help="An optional boolean parameter. If set to 'true', "
                                         "the site's never cache rules will be cleared.")
site_cache_rule_parser.add_argument('--clear_cache_headers_rules', default='',
                                    help="An optional boolean parameter. If set to 'true', "
                                         "the site's cache header rules will be cleared.")
site_cache_rule_parser.add_argument('--log', default='INFO')
site_cache_rule_parser.set_defaults(func=u_cacherule)

site_advanced_cache_parser = site_subparsers.add_parser('advanced-cache',
                                                        help='Use this operation to modify advanced caching settings.',
                                                        usage='incap site cache advanced-cache param value site_id')
site_advanced_cache_parser.add_argument('--api_id', help='API authentication identifier.')
site_advanced_cache_parser.add_argument('--api_key', help='API authentication identifier.')
site_advanced_cache_parser.add_argument('param', help="Name of configuration parameter to set. See table below.")
site_advanced_cache_parser.add_argument('value', help="According to the param value. See table below.")
site_advanced_cache_parser.add_argument('site_id', help='Numeric identifier of the site to operate on.')
site_advanced_cache_parser.add_argument('--log', default='INFO')
site_advanced_cache_parser.set_defaults(func=u_advanced)

account_parser = subparsers.add_parser('account',
                                       help='Used to add, delete and configure Incapsula accounts.',
                                       usage='incap account <command> [options]')
account_subparsers = account_parser.add_subparsers(description='valid subcommands',
                                                   help='additional help')
account_add_parser = account_subparsers.add_parser('add',
                                                   help='Use this operation to add a new account that '
                                                        'should be managed by the account of the API client '
                                                        '(the parent account). The new account will be configured '
                                                        'according to the preferences set for the '
                                                        'parent account by Incapsula.',
                                                   usage='incap account add [options] email')
account_add_parser.add_argument('--api_id', help='API authentication identifier.')
account_add_parser.add_argument('--api_key', help='API authentication identifier.')
account_add_parser.add_argument('email', help='Email address. For example: "joe@example.com".')
account_add_parser.add_argument('--parent_id', '--parent_id=', default='',
                                help='The newly created accounts parent id. '
                                     'If not specified, the invoking account will be assigned as the parent.')
account_add_parser.add_argument('--user_name', '--user_name=', default='',
                                help='The account owners name. For example: "John Doe".')
account_add_parser.add_argument('--plan_id', '--plan_id=', default='',
                                help='An identifier of the plan to assign to '
                                     'the new account. For example, ent100 for the Enterprise 100 plan.')
account_add_parser.add_argument('--ref_id', '--ref_id=', default='',
                                help='Customer specific identifier for this operation.')
account_add_parser.add_argument('--account_name', '--account_name=', default='', help='Account name.')
account_add_parser.add_argument('--log_level', '--log_level=<full,security,none,default>', default='',
                                help='Available only for Enterprise Plan customers that purchased '
                                     'the Logs Integration SKU. Sets the log reporting level for the site. '
                                     'Options are “full”, “security”, “none” and "default"')
account_add_parser.add_argument('--logs_account_id', default='',
                                help='Available only for Enterprise Plan customers that purchased the '
                                     'Logs Integration SKU. Numeric identifier of the account that purchased the '
                                     'logs integration SKU and which collects the logs. '
                                     'If not specified, operation will be performed on the account '
                                     'identified by the authentication parameters')
account_add_parser.add_argument('--log', default='INFO')
account_add_parser.set_defaults(func=c_account)

account_audit_parser = account_subparsers.add_parser('audit',
                                                     help='Use this operation to get audit events for an account.',
                                                     usage='incap account audit [options]')
account_audit_parser.add_argument('--api_id', help='API authentication identifier.')
account_audit_parser.add_argument('--api_key', help='API authentication identifier.')
account_audit_parser.add_argument('--account_id',
                                  help='Numeric identifier of the account to operate on. If not specified, '
                                       'operation will be performed on the account identified by the authentication'
                                       ' parameters.')
account_audit_parser.add_argument('--time_range', default='today',
                                  help='Time range to fetch data for. For a detailed description, '
                                       'i.e. last_7_days | last_30_days | last_90_days | month_to_date')
account_audit_parser.add_argument('--start', default='',
                                  help='Start date in milliseconds since 1970; '
                                       'All dates should be specified as number of milliseconds since midnight 1970 '
                                       '(UNIX time * 1000).')
account_audit_parser.add_argument('--end', default='', help='End date in milliseconds since 1970; '
                                                            'All dates should be specified as number of milliseconds '
                                                            'since midnight 1970 (UNIX time * 1000).')
account_audit_parser.add_argument('--type', default='',
                                  help='The api key of the event type, such as audit.account_login.')
account_audit_parser.add_argument('--page_size', default='50',
                                  help='The number of objects to return in the response. Default: 50.')
account_audit_parser.add_argument('--page_num', default='0', help='The page to return starting from 0. Default: 0.')
account_audit_parser.add_argument('--log', default='INFO')
account_audit_parser.set_defaults(func=r_audit)

account_status_parser = account_subparsers.add_parser('status',
                                                      help='Use this operation to get information '
                                                           'about the account of the API client or '
                                                           'one of its managed accounts.',
                                                      usage='incap account status [options]')
account_status_parser.add_argument('--api_id', help='API authentication identifier.')
account_status_parser.add_argument('--api_key', help='API authentication identifier.')
account_status_parser.add_argument('--account_id',
                                   help='Numeric identifier of the account to operate on. If not specified, '
                                        'operation will be performed on the account identified by '
                                        'the authentication parameters.')
account_status_parser.add_argument('--log', default='INFO')
account_status_parser.set_defaults(func=r_account)

account_list_parser = account_subparsers.add_parser('list',
                                                    help='Use this operation to get audit events for an account.',
                                                    usage='incap account audit [options]')
account_list_parser.add_argument('--api_id', help='API authentication identifier.')
account_list_parser.add_argument('--api_key', help='API authentication identifier.')
account_list_parser.add_argument('--account_id',
                                 help='Numeric identifier of the account to operate on. If not specified, '
                                      'operation will be performed on the account identified by the authentication '
                                      'parameters.')
account_list_parser.add_argument('--page_size', default='50',
                                 help='The number of objects to return in the response. Default: 50.')
account_list_parser.add_argument('--page_num', default='0', help='The page to return starting from 0. Default: 0.')
account_list_parser.add_argument('--log', default='INFO')
account_list_parser.set_defaults(func=r_accounts)

account_subList_parser = account_subparsers.add_parser('sublist',
                                                       help='Use this operation to get audit events for an account.',
                                                       usage='incap account audit [options]')
account_subList_parser.add_argument('--api_id', help='API authentication identifier.')
account_subList_parser.add_argument('--api_key', help='API authentication identifier.')
account_subList_parser.add_argument('--account_id',
                                    help='Numeric identifier of the account to operate on. If not specified, '
                                         'operation will be performed on the account identified by the authentication'
                                         ' parameters.')
account_subList_parser.add_argument('--page_size', default='50',
                                    help='The number of objects to return in the response. Default: 50.')
account_subList_parser.add_argument('--page_num', default='0', help='The page to return starting from 0. Default: 0.')
account_subList_parser.add_argument('--log', default='INFO')
account_subList_parser.set_defaults(func=r_subaccount)


def main(args=None):
    args = parser.parse_args(args=args)
    args.func(args)


def testing(args=None):
    args = parser.parse_args(args=args)
    return args.func(args)
