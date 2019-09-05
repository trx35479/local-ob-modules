import time
from Sites.cache import Cache
from Integration.clapps import r_clapps
import logging


class Site:
    def __init__(self, data):
        self.res_message = data.get('res_message') or None
        self.domain = data.get('domain') or ''
        self.site_id = data.get('site_id') or int
        self.account_id = data.get('account_id') or ''
        self.active = data.get('active') or ''
        self.extended_ddos = data.get('extended_ddos') or int
        self.res = data['res']
        self.response_message = data.get('res_message') or ''
        self.display_name = data.get('display_name') or ''
        self.acceleration_level = data.get('acceleration_level') or ''
        self.site_creation_date = data.get('site_creation_date') or int
        self.status = data.get('status') or ''
        self.dns = data.get('dns') or []
        self.additionalErrors = data.get('additionalErrors') or []
        self.ips = data.get('ips') or []
        self.debug_info = data.get('debug_info') or []
        self.login_protect = data.get('login_protect') or {}
        self.original_dns = data.get('original_dns') or []
        self.performance_configuration = data.get('performance_configuration') or {}
        self.sealLocation = data.get('sealLocation') or {}
        self.security = data.get('security') or None
        self.waf_rules = self.security['waf']['rules'] or []
        self.siteDualFactorSettings = data.get('siteDualFactorSettings') or {}
        self.ssl = data.get('ssl') or {}
        self.warnings = data.get('warnings') or []
        self.authentication_methods = self.login_protect.get('authentication_methods') or []
        self.policies = data.get('policies') or None
        if self.policies is not None:
            if self.policies.get('incap_rules'):
                self.incap_rules = self.policies['incap_rules']['All']
            if self.policies.get('delivery_rules'):
                self.adr_rules = self.policies['delivery_rules'] or {}
        elif data.get('incap_rules'):
            self.incap_rules = data.get('incap_rules')
            self.adr_rules = None
        self.clapps = None
        self.cache = Cache(self.performance_configuration)

    def get_clapps(self, cl_id):
        if self.clapps is None:
            self.clapps = r_clapps()
            client = self.clapps['clientAppTypes'][cl_id[0]] + ' with client name ' + self.clapps['clientApps'][cl_id[0]]
            return client
        else:
            client = self.clapps['clientAppTypes'][cl_id[0]] + ' with client name ' + self.clapps['clientApps'][cl_id[0]]
            return client

    def get_waf_rules(self):
        return self.waf_rules

    def get_domain(self):
        return self.domain

    def get_id(self):
        return self.site_id

    def log(self):
        divide = '-------------------------------------------------------------------------------------------------'
        thistime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.site_creation_date / 1000.0))
        print(divide)
        print('Site ID: %s' % self.site_id)
        print('Domain: %s' % self.domain)
        print('Display Name = %s' % self.display_name)
        print('Account ID: %s' % self.account_id)
        print('Site status: %s' % self.status)
        print('Site Creation Date: %s' % thistime)
        print('Active Status = %s' % self.active)
        print('Extended DDoS = %s' % self.extended_ddos)
        print('Seal Location = %s' % self.sealLocation['name'])
        print('Acceleration Level: %s' % self.acceleration_level)

        print(divide)
        print('Current DNS information is set to the following:')
        print(divide)
        for dns in self.dns:
            for dns_ip in dns['set_data_to']:
                print('The current %s Record for %s is %s\r' %
                             (dns['set_type_to'], dns['dns_record_name'], dns_ip))

        print(divide)
        print('Original DNS information was set to the following:')
        print(divide)
        for o_dns in self.original_dns:
            for o_dns_ip in o_dns['set_data_to']:
                print('The original %s Record for %s was %s\r' %
                      (o_dns['set_type_to'], o_dns['dns_record_name'], o_dns_ip))
        print(divide)

        if self.additionalErrors:
            print('Additional Errors:')
            for err in self.additionalErrors:
                logging.error('%s'.join(err))
        else:
            print("No additional Errors")

        print(divide)

        for ip in self.ips:
            print('Origin Server IP/CNAME: %s' % ip)
        print(divide)
        if self.login_protect.get('enabled'):
            print('Login Protect details:')
            print('Allow All Users = %s' % self.login_protect['allow_all_users'])
            print('Authentication Method(s) = %s.' %
                         ', '.join(self.login_protect['authentication_methods']))
            print('Send Login Protect Notifications = %s' % self.login_protect['send_lp_notifications'])
            for users in self.login_protect['specific_users_list']:
                print('Login Protect UserName = {name}, Email = {email} '
                             'and Status = {status}'.format(**users))
            print('URL(s) = %s' % ', '.join(self.login_protect['urls']))


        #print('Site Dual Factor Settings = %s' % self.siteDualFactorSettings)
        #print('SSL = %s' % self.ssl)

        #print('PerformanceConfiguration = %s' % self.performance_configuration)
        print(divide)

        if 'acls' in self.security:
            print('ACL settings are as follows:')
            for aclRules in self.security['acls']['rules']:
                if aclRules['id'] == 'api.acl.blacklisted_ips':
                    print('The following IPs are blacklisted: %s' % ', '.join(aclRules['ips']))
                    if 'exceptions' in aclRules:
                        print('Blacklisted IPs Exceptions follow:')

                        for exception in aclRules['exceptions']:
                            self.site_exceptions(exception)

                elif aclRules['id'] == 'api.acl.whitelisted_ips':
                    print('The following IPs are whitelisted: %s' % ', '.join(aclRules['ips']))

                elif aclRules['id'] == 'api.acl.blacklisted_countries':
                    print('The following countries are blacklisted: %s' % ', '.join(aclRules['geo']['countries']))
                    if 'exceptions' in aclRules:
                        print('Blacklisted Countries Exceptions follow:')

                        for exception in aclRules['exceptions']:
                            self.site_exceptions(exception)

                elif aclRules['id'] == 'api.acl.blacklisted_urls':

                    for url in aclRules['urls']:
                        print('URL is blacklisted: url= %s pattern= %s.'
                                     % (''.join(url['value']), ''.join(url['pattern'])))
                else:
                    print("Nothing is being blacklisted or whitelisted.")
        else:
            print(divide)
            print("No ACLs")
        print(divide)

        print('Security settings are as follows:')
        print(divide)

        for secRule in self.security["waf"]["rules"]:

            if secRule['name'] == 'Bot Access Control':
                print('{name} setting are: Block Bad Bots={block_bad_bots} '
                             'and Challenge Suspected Bots={challenge_suspected_bots}.'.format(**secRule))

                if 'exceptions' in secRule:
                    print('Bot Exceptions follow:')

                    for exception in secRule['exceptions']:
                        self.site_exceptions(exception)

            elif secRule['name'] == 'DDoS':
                print('{name} setting are: DDoS Activation Mode={activation_mode_text} '
                             'and DDoS Traffic Threshold={ddos_traffic_threshold}.'.format(**secRule))

                if 'exceptions' in secRule:
                    print('DDoS Exceptions follow:')

                    for exception in secRule['exceptions']:
                        self.site_exceptions(exception)
            else:
                print('{name} is set to {action_text}.'.format(**secRule))

        print('\nSSL info following:')
        print('SSL detected: {0}, detected status: {1}.'
                     .format(self.ssl['origin_server']['detected'], self.ssl['origin_server']['detectionStatus']))

        if self.ssl['origin_server']['detected'] == 'True':

            if 'validation_method' in self.ssl['generated_certificate']:
                print('Validation has been set to {0}.'.format(self.ssl['generated_certificate']['validation_method']))

                if self.ssl['generated_certificate']['validation_method'] == 'dns':

                    for v_data in self.ssl['generated_certificate']['validation_data']:
                        print('Please set the TXT record for {0} to {1}.'
                              .format(v_data['dns_record_name'], v_data['set_data_to']))
                print('The SSL certificate status is {0}.'.format(self.ssl['generated_certificate']['validation_status']))
                print('The CA is {0}.'.format(self.ssl['generated_certificate']['ca']))
                print('The SAN cert is for {0}.'.format(self.ssl['generated_certificate']['san']))

            else:
                print('SSL has been detected but no certificate has been created/validated yet.')

        print('\nWarnings for the following:')

        for warning in self.warnings:
            print('Warning Type= %s, Set type to= %s, with IP/CNAME=%s'
                  % (warning['type'], warning['set_type_to'], ', '.join(warning['set_data_to'])))
        #print('Response = %s' % self.res)
        #print('Response Message = %s' % self.response_message)
        #print('Debug Info = %s' % self.debug_info)

    def site_exceptions(self, data):
        #print('{values}'.format(**data))
        for item in data['values']:
            #pprint('{id}'.format(**item))
            if item['id'] == 'api.rule_exception_type.client_ip':
                print('-------------------------------------------------------------------------------------------\n|\n'
                      '| IP Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ', '.join(item['ips']))
            elif item['id'] == 'api.rule_exception_type.user_agent':
                print('-------------------------------------------------------------------------------------------\n|\n'
                      '| User Agent Exception ID: {id}'.format(**data) + ' -  Exception for client app type: %s\n|' % ', '.join(item['user_agents']))
            elif item['id'] == 'api.rule_exception_type.url':
                for url in item['urls']:
                    print('-------------------------------------------------------------------------------------------\n|\n'
                          '| Url Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ''.join(url['value']))
            elif item['id'] == 'api.rule_exception_type.country':
                print('-------------------------------------------------------------------------------------------\n|\n'
                      '| Country Exception ID: {id}'.format(**data) + ' - Exception for client app type: %s\n|' % ', '.join(item['geo']['countries']))
            elif item['id'] == 'api.rule_exception_type.client_app_id':
                print('-------------------------------------------------------------------------------------------\n|\n'
                      '| Client Application Exception ID: {id}'.format(**data) + ' - '
                                                                                 'Exception for client app type: %s\n|' % ''.join(self.get_clapps(item['client_apps'])))
