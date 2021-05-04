from base.base import Base
from config.user import User
from . import ims
from . import log


class TeamList(Base):

    def add_member(self,
                   username='wellyadmin',
                   currency="CNY",
                   firstName="welly",
                   isAgent=False,
                   level=1,
                   mobile="",
                   parentAccount="ssh002",
                   parentId=136,   # 新增的時候打上 parentAccount 帳號, 會有給parentId
                   password="a780598d54551cd786db3fc052cd4054d6267cbc",
                   playerId="add00001",
                   remark="",
                   repassword="aa111222",
                   vipId="a582d64f-45e2-4769-94b3-2573b59279a3",
                   ):

        url = ims.url_add_member()
        _, token = self.ims_login(username)
        headers = self.header(token)
        data = {
            'currency': currency,
            'firstName': firstName,
            'isAgent': isAgent,
            'level': level,
            'mobile': mobile,
            'parentAccount': parentAccount,
            'parentId': parentId,
            'password': password,
            'playerId': playerId,
            'remark': remark,
            'repassword': repassword,
            'vipId': vipId,
        }

        r = self.s.post(url, headers=headers, json=data)
        log(f"Add member: {r.json()}")

        return r.status_code, r.json()

    def ag_team_list_search(self,
                             username='wellyadmin',
                             status='0',
                             level='0',
                             searchValue='sh002',
                             searchField='AGENT',
                             sortColumn='ACCOUNT',
                             sort='ASC',
                             limit='25',
                             offset='0',):
        url = ims.url_ag_team_list()
        _, token = self.ims_login(username)
        headers = self.header(token)
        params = {
            'status': status,
            'level': level,
            'searchValue': searchValue,
            'searchField': searchField,
            'sortColumn': sortColumn,
            'sort': sort,
            'limit': limit,
            'offset': offset,
        }
        r = self.s.get(url, headers=headers, params=params)
        log(f"Ag team list: {r.json()}")

        return r.status_code, r.json()

    def get_level(self, username='wellyadmin', account=None):
        url = ims.url_get_level()
        _, token = self.ims_login(username)
        headers = self.header(token)
        params = {
            'account': account
        }
        r = self.s.get(url, headers=headers, params=params)
        log(f"Get level: {r.json()}")

        return r.json()

    def add_agent(self,
                  username='wellyadmin',
                  account="sshadd00001",
                  commissionPct=0.4,    # 成本佔成
                  createFp="6bad4e7168527a1e7cebece584d447e6",
                  currency="CNY",
                  initGroupPointPermission=True,
                  isAgent=True,
                  level=1,
                  minDeposit="1",
                  minEffectivePlayer="50",
                  minRevenue="0",
                  minValidBet="0",
                  mobile="",
                  name="welly",
                  parentAccount=None,
                  parentId=0,
                  password="2ee271b2982855593b1e2c9a98ba363b74f6d76f",
                  remark="",
                  repassword="aa111222",
                  vipId="ec6f39f7-142f-4897-bf5d-70fa1035e28a",
                  ):
        url = ims.url_add_agent()
        _, token = self.ims_login(username)
        headers = self.header(token)
        data = {
            'account': account,
            'commissionPct': commissionPct,
            'createFp': createFp,
            'currency': currency,
            'gpSettings': [
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "CARD365"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "JDB"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "AE_C"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "CQ9"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "KINGMAKER"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "KY"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "DS"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "VG"
               },
               {
                   "status": True,
                   "productType": "CHESS",
                   "gameProvider": "LC"
               },
               {
                   "status": True,
                   "productType": "ESPORTS",
                   "gameProvider": "TF"
               },
               {
                   "status": True,
                   "productType": "ESPORTS",
                   "gameProvider": "ESPORTSBULL"
               },
               {
                   "status": True,
                   "productType": "ESPORTS",
                   "gameProvider": "AE_ES2"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "VG"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "SIMPLEPLAY"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "SA"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "MW"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "JDB"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "GGAMING"
               },
               {
                   "status": True,
                   "productType": "MPG",
                   "gameProvider": "CQ9"
               },
               {
                   "status": True,
                   "productType": "LOTTERY",
                   "gameProvider": "VSL"
               },
               {
                   "status": True,
                   "productType": "LOTTERY",
                   "gameProvider": "VR"
               },
               {
                   "status": True,
                   "productType": "LOTTERY",
                   "gameProvider": "GW"
               },
               {
                   "status": True,
                   "productType": "LOTTERY",
                   "gameProvider": "GPI"
               },
               {
                   "status": True,
                   "productType": "LOTTERY",
                   "gameProvider": "AE_LOT"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "DG"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "PT"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "BBIN"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "SEXYLINE"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "SA"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "ALLBET"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "SEXYBCRT"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "WM"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "MG"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "VENUS"
               },
               {
                   "status": True,
                   "productType": "LIVE",
                   "gameProvider": "EVO"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "PP"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "RT"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "PS"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "PT"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "BBIN"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "RW"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "SIMPLEPLAY"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "JDB"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "AE_GAMING"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "MW"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "CQ9"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "UFASLOT"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "SA"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "SEA"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "JOKER"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "PG"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "AMEBA"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "MG"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "RICH88"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "JILI"
               },
               {
                   "status": True,
                   "productType": "EGAME",
                   "gameProvider": "VT"
               },
               {
                   "status": True,
                   "productType": "MINI_GAME",
                   "gameProvider": "GW"
               },
               {
                   "status": True,
                   "productType": "MINI_GAME",
                   "gameProvider": "GPI"
               },
               {
                   "status": True,
                   "productType": "MINI_GAME",
                   "gameProvider": "AE_LOT"
               },
               {
                   "status": True,
                   "productType": "FINANCE",
                   "gameProvider": "BO"
               },
               {
                   "status": True,
                   "productType": "ANIMAL",
                   "gameProvider": "TRC"
               },
               {
                   "status": True,
                   "productType": "ANIMAL",
                   "gameProvider": "SV"
               },
               {
                   "status": True,
                   "productType": "ANIMAL",
                   "gameProvider": "SPR168"
               },
               {
                   "status": True,
                   "productType": "ANIMAL",
                   "gameProvider": "S128"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "UGAMING"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "UFABET"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "SBOBET"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "SABA"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "CMDBET"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "BTI"
               },
               {
                   "status": True,
                   "productType": "SPORTS",
                   "gameProvider": "AE_CRICKET"
               }
        ],
            'initGroupPointPermission': initGroupPointPermission,
            'isAgent': isAgent,
            'level': level,
            'minDeposit': minDeposit,
            'minEffectivePlayer': minEffectivePlayer,
            'minRevenue': minRevenue,
            'minValidBet': minValidBet,
            'mobile': mobile,
            'name': name,
            'parentAccount': parentAccount,
            'parentId': parentId,
            'password': password,
            'remark': remark,
            'repassword': repassword,
            'vipId': vipId,
        }
        r = self.s.post(url, headers=headers, json=data)
        log(f"Add agent: {r.json()}")

        return r.status_code, r.json()


    def agentSite_login(self,
                        username='add111',
                        fp='1c640948924097806bca62dd5302134c',
                        pwd='25cbe87f8d463aa17eb9a10cf08fc72c1618d89f'
                        ):
        url = ims.url_agentSite_login()
        headers = {
                    'accept': '*/*',
                    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                    'authorization': 'undefined',
                    'content-length': '119',
                    'content-type': 'application/json;charset=UTF-8',
                    'origin': 'https://ae-ag.stgdevops.site',
                    'referer': 'https://ae-ag.stgdevops.site/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/90.0.4430.85 Safari/537.36',

        }
        data = {'account': username,
                'loginFp': fp,
                'password': pwd}
        r = self.s.post(url, headers=headers, json=data)
        log(f'Agent site login: {r.status_code}')

        return r.status_code

    def agent_status_update(self,
                            username='wellyadmin',
                            ag_id=None,
                            status='STATUS',
                            value=None
                            ):
        url = ims.url_update_ag_status(agent_id=ag_id)
        _, token = self.ims_login(username)
        headers = self.header(token)
        data = {'field': status,
                'value': value}
        r = self.s.put(url, headers=headers, json=data)
        log(f"Agent status update: {r.status_code}, value: {value}")
        if r.status_code != 204:
            raise ValueError(f'Update agent status failed, failed value: {value}')

        return r.status_code


    def agent_point(self,
                    username='wellyadmin',
                    point=None,
                    txn_type='ADD' or 'SUBTRACT',
                    down_line_id=465,
                    method='PUT',
                    upLineLevel=0,
                    start=0,
                    end=0,
                    sortColumn='CREATE_TIME',
                    sort='DESC',
                    limit=25,
                    offset=0,
                    ):
        url = ims.url_ag_point()
        _, token = self.ims_login(username)
        headers = self.header(token)

        if method == 'PUT':
            data = {'downLineId': down_line_id,
                    'point': point,
                    'txnType': txn_type}
            r = self.s.put(url, headers=headers, json=data)
            log(f'Agent point change status code: {r.status_code}')

            if r.status_code != 204:
                raise ValueError(f'Agent point change failed: {r.status_code}')
            return r.status_code
        elif method == 'GET':
            params = {'upLineLevel': upLineLevel,
                      'end': end,
                      'start': start,
                      'sortColumn': sortColumn,
                      'sort': sort,
                      'limit': limit,
                      'offset': offset,
                      'startTime': start,
                      'endTime': end}
            r = self.s.get(url, headers=headers, params=params)
            log(f'Agent point report: {r.json()}, Status: {r.status_code}')

            return r.status_code, r.json()

        else:
            raise KeyError('Method should be put or get.')


