class User:

    def __init__(self, user):
        self.user = user

    user_info = {'wellyadmin': {'user': 'wellyadmin',
                                'pwd': '64e89cab6f9b5560931d87399d916faf08e95c49'},
                 'wellyview': {'user': 'wellyview',
                               'pwd': '8722599303c1dc741ee44265fa7177cd4637b569'}}

    def username(self):
        return self.user_info[self.user]['user']

    def pwd(self):
        return self.user_info[self.user]['pwd']
