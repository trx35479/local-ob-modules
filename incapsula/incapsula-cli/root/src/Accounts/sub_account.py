class SubAccount:
    def __init__(self, data):
        self.sub_account_id = data.get('sub_account_id') or ''
        self.sub_account_name = data.get('sub_account_name') or ''
        self.support_level = data.get('support_level') or ''

    def log(self):
        return '-------------------------------------------------------------------------------------------------\n' \
               'Sub Account Name: %s\nSub Account ID: %s\nSupport Level: %s' \
               % (self.sub_account_name, self.sub_account_id, self.support_level)
