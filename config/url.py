class Url:

    def __init__(self, env):
        self.env = env

    stg = 'https://ae-boapi.stgdevops.site/ae-ims/api/v1/'

    _login = 'login'
    login = {'stg': stg + _login}

    def url_login(self):
        return self.login[self.env]

    # ads
    _ads = 'ads'
    ads = {'stg': stg + _ads}

    def url_ads(self):
        return self.ads[self.env]

    # player resource
    _players_list_search = 'players/list/search'
    players_list_search = {'stg': stg + _players_list_search}

    def url_players_list_search(self):
        return self.players_list_search[self.env]



