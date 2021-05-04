class ImsUrl:

    def __init__(self, env='stg'):
        self.env = env

        base = f'https://ae-boapi.{env}devops.site/ae-ims/api/v1/'

        login =     'login'
        ads =       'ads'
        
        self.login =    base + login
        self.ads =      base + ads

        # User roles
        user_roles = 'userroles/'

        superadmin = 'Super%20Admin'

        self.user_roles_setting = base + user_roles + superadmin
        
        # Player resource

        status =            'status'
        notes =             'notes'
        transactions =      'transactions/'
        player_wallets =    'playerwallets/'
        ulagent =           'ulagent/'
        players =           'players/'
        ulagentSite =       'ulagentSite/'

        kick =              'kick'
        manualbalance =     'manualbalance'
        search =            'search/'
        player =            'player'
        list =              'list/'
        login =             'login/'
        point =             'point/'

        lookup =            'lookup'
        level =             'level'

        self.status =               status
        self.notes =                notes
        self.players =              base + players
        self.players_kick =         base + players + kick
        self.player_wallets =       base + player_wallets + manualbalance
        self.players_list_search =  base + players + list + search.strip('/')
        self.players_list_lookup =  base + players + list + lookup
        self.transactions_search =  base + transactions + search.strip('/')
        self.add_agent =            base + ulagent
        self.add_member =           base + ulagent + player
        self.ag_team_list =         base + ulagent + search.strip('/')
        self.get_level =            base + ulagent + search + level
        self.ag_point =             base + ulagent + point.strip('/')
        self.agentSite_login =      base + ulagentSite + login.strip('/')

    def url_login(self):
        return self.login

    def url_ads(self):
        return self.ads

    # Player resources
    def url_players_list_search(self):
        return self.players_list_search

    def url_add_player(self):
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

    def url_add_member(self):
        return self.add_member

    def url_ag_team_list(self):
        return self.ag_team_list

    def url_get_level(self):
        return self.get_level

    def url_add_agent(self):
        return self.add_agent

    def url_agentSite_login(self):
        return self.agentSite_login

    def url_update_ag_status(self, agent_id):
        return self.add_agent + str(agent_id) + '/update'

    def url_ag_point(self):
        return self.ag_point

    def url_user_roles_setting(self):
        return self.user_roles_setting
