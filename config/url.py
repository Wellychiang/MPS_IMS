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
    _players = 'players'
    _list = '/list'
    _status = '/status'
    _notes = '/notes'
    _players_kick = f'{_players}/kick'
    _players_list_search = f'{_players}{_list}/search'
    _players_list_lookup = f'{_players}{_list}/lookup'

    players = {'stg': stg + _players}
    players_kick = {'stg': stg + _players_kick}
    players_list_search = {'stg': stg + _players_list_search}
    players_list_lookup = {'stg': stg + _players_list_lookup}

    def url_players_list_search(self):
        return self.players_list_search[self.env]

    def url_players(self):
        return self.players[self.env]

    def url_players_list_lookup(self):
        return self.players_list_lookup[self.env]

    def url_players_playerid_status(self, playerid):
        return f'{self.players[self.env]}/{playerid}{self._status}'

    def url_players_playerid(self, playerid):
        return f'{self.players[self.env]}/{playerid}'

    def url_players_playerid_notes(self, playerid):
        return f'{self.players[self.env]}/{playerid}{self._notes}'

    # transactions, 會員列表 > 會員信息 > 人工餘額調整(搜索)
    _transactions = 'transactions'
    _transactions_search = f'{_transactions}/search'

    transactions_search = {'stg': stg + _transactions_search}

    def url_transactions_search(self):
        return self.transactions_search[self.env]




