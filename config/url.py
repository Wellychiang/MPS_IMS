class ImsUrl:

    def __init__(self, env='stg'):
        self.env = env

        base = f'https://ae-boapi.{env}devops.site/ae-ims/api/v1/'

        login = 'login'
        ads = 'ads'
        
        self.login = base + login
        self.ads = base + ads
        
        # Player resource
        players = 'players/'
        status = 'status'
        notes = 'notes'
        transactions = 'transactions/'
        player_wallets = 'playerwallets/'
        
        kick = 'kick'
        manualbalance = 'manualbalance'
        list = 'list/'
        search = 'search'
        
        lookup = 'lookup'

        self.status = status
        self.players = base + players
        self.notes = notes
        self.players_kick = base + players + kick
        self.player_wallets = base + player_wallets + manualbalance
        self.players_list_search = base + players + list + search
        self.players_list_lookup =  base + players + list + lookup
        self.transactions_search = base + transactions + search
        

    def url_login(self):
        return self.login

    def url_ads(self):
        return self.ads

    # Player resources
    def url_players_list_search(self):
        return self.players_list_search

    def url_players(self):
        return self.players

    def url_players_list_lookup(self):
        return self.players_list_lookup

    def url_players_playerid_status(self, playerid):
        return f'{self.players}{playerid}/{self.status}'

    def url_players_playerid(self, playerid):
        return f'{self.players}{playerid}'

    def url_players_playerid_notes(self, playerid):
        return f'{self.players}{playerid}/{self.notes}'

    def url_transactions_search(self):
        return self.transactions_search

    def url_player_wallets(self):
        return self.player_wallets




