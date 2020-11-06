from base.base import Base
from config.url import Url


class PlayerResource(Base):

    def players_list_search(self, language='2',
                            limit='25',
                            createdtend='-1',
                            createdtstart='-1',
                            offset='0',
                            playerid='welly',
                            playeridexactmatch='False',
                            sort='ASC',
                            sortcolumn='playerid',
                            firstname=None,
                            totalavailablefrom=None,
                            totalavailableto=None,
                            switch_create=True,
                            totaldepositfrom=None,
                            totaldepositto=None,
                            totalwithdrawalfrom=None,
                            totalwithdrawalto=None,
                            agentidexactmatch=None,
                            agentupline=None,
                            ulagent=None,
                            affiliateupline=None,
                            bankaccount=None,
                            vipid=None,
                            tags=None,
                            mobile=None,
                            hasverifiedmobile=None,
                            email=None,
                            im1=None,
                            im2=None,
                            dl=None,
                            lan=None):
        env = Url(self.env)
        url = env.url_players_list_search()

        _, get_token = self.login()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Authorization': get_token['token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': '*/*',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = {
            'language': language,                       # int, default value: 2
            'limit': limit,                             # 一頁要顯示的資料數
            'createdtend': createdtend,                 # 註冊時間範圍(日期类型)
            'createdtstart': createdtstart,
            'loginend': createdtend,                    # 上次登入時間的範圍(日期类型)
            'loginstart': createdtstart,
            'offset': offset,                           # 從第幾筆開始往下顯示, offset=0, 25, 50, 就是在limit=25的情況下顯示第1,2,3頁
            'playerid': playerid,                       # username
            'playeridexactmatch': playeridexactmatch,   # 精準搜尋與否
            'sort': sort,                               # (String)Default value : ASC, available: ASC, DESC
            'sortcolumn': sortcolumn,                   # 搜尋出來資料後的排序是以哪個參數進行sort
            'totalavailablefrom': totalavailablefrom,   # 總餘額時間(金額類型)
            'totalavailableto': totalavailableto,
            'totaldepositfrom': totaldepositfrom,       # 總存款時間(金額類型)
            'totaldepositto': totaldepositto,
            'totalwithdrawalfrom': totalwithdrawalfrom, # 總提款時間(金額類型)
            'totalwithdrawalto': totalwithdrawalto,
            'firstname': firstname,                     # 真實姓名
            'agentidexactmatch': agentidexactmatch,     # 代理帳號模糊搜索
            'agentupline': agentupline,                 # 代理帳號
            'ulagent': ulagent,                         # 代理團隊, True=代理欄位會變成成代理團隊欄位
            'affiliateupline': affiliateupline,         # 老待新上線(沒有模糊搜尋)
            'bankaccount': bankaccount,                 # 銀行帳號
            'vipid': vipid,                             # 層級組別
            'tags': tags,                               # 標籤名稱
            'mobile': mobile,                           # 手機號碼(聯絡方式)
            'hasverifiedmobile': hasverifiedmobile,     # 已驗證(手機號碼)
            'email': email,                             # 電子信箱(聯絡方式)
            'im1': im1,                                 # 會進行客製化的咚咚(聯絡方式)
            'im2': im2,                                 # 會進行客製化的咚咚(聯絡方式)
            'dl': dl,                                   # 匯出(先不弄)
            'lan': lan                                  # 匯出顯示的語言(同上)
        }

        if switch_create is True:
            params.pop('loginend')
            params.pop('loginstart')

        elif switch_create is False:
            params.pop('createdtend')
            params.pop('createdtstart')

        r = self.s.get(url, headers=headers, params=params)
        self.log.info(f'{str(r.json()).encode("utf-8").decode("cp950", "ignore")}')
        return r.status_code, r.json()

    def players_list_lookup(self, username='welly'):
        env = Url(self.env)
        url = env.url_players_list_lookup()

        _, get_token = self.login()
        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Authorization': get_token['token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': '*/*',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = {
            'q': username
        }
        r = self.s.get(url, headers=headers, params=params)
        self.log.info(f'response: {r.json()}')
        return r.status_code, r.json()

    def players(self, username='welly', user_num=10):
        env = Url(self.env)
        url = env.url_players()

        _, get_token = self.login()
        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Authorization': get_token['token'],
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
        }

        data = {"playerid": username + str(user_num),
                "pin":None,
                "currency":"CNY",
                "password": "1aa824dd774a620e3f9b673af91539985dd32001",
                "firstname":"wade",
                "lastname":None,
                "birthdate":None,
                "birthday":None,
                "nationality":None,
                "mobile":None,
                "email":None,
                "country":"",
                "address":None,
                "city":"",
                "state":None,
                "postcode":None,
                "regip":"123.51.187.178",
                "regfingerprint":None,
                "im1":None,"im2":None,
                "loginError":0,
                "status":1,
                "vipid":"ec6f39f7-142f-4897-bf5d-70fa1035e28a",
                "tagids":None,
                "tagnames":None,
                "tiers":"wade10",
                "affiliateid":None,
                "affiliatestatus":0,
                "language":2,
                "logintime":None,
                "loginip":None,
                "logindevice":None,
                "loginplatform":None,
                "loginfingerprint":None,
                "registeredby":0,
                "createdate":1604558363968,
                "activedate":1604558363968,
                "lastupdate":None,
                "updateby":"wellyadmin",
                "lastlogintime":None,
                "logincount":0,
                "captchauuid":None,
                "captcha":None,
                "portalid":None,
                "promoStatus":1,
                "internalplayer":False,
                "onlinestatus":0,
                "addparent":False,
                "withdrawid":None,
                "settle":False,
                "agentid":None,
                "vendorId":None,
                "totalavailable":None,
                "connsleerror":None,
                "packagevalue":None,
                "pic1id":None,
                "pic2id":None,
                "pic1":None,
                "pic2":None,
                "affiliatebindtime":None,
                "hasverifiedmobile":False,
                "hasverifiedmobilestr":None,
                "displayname":None,
                "showforec":False,
                "upLineAgents":None,
                "ulagentid":None,
                "ulagentaccount":None,
                "remark":None,
                "mask":False,
                "lineUserId":None,
                "verificationcode":None}

        r = self.s.post(url, headers=headers, json=data)
        self.log.info(r.json())
        return r.status_code, r.json()

    def players_playerid(self, username='welly'):
        env = Url(self.env)
        url = env.url_players_playerid(username)

        _, get_token = self.login()
        headers = {
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization': get_token['token'],
            'Connection': 'keep-alive',
            'Host': 'ae-boapi.stgdevops.site',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        }

        r = self.s.get(url, headers=headers)
        self.log.info(r.json())

        return r.status_code, r.json()

    def players_playerid_status(self, username='welly', status=1):
        env = Url(self.env)
        url = env.url_players_playerid_status(username)
        print(url)
        _, get_token = self.login()

        headers = {
            'Authorization': get_token['token'],
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'ae-boapi.stgdevops.site',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
        }

        data = {
            'status': status
        }

        r = self.s.put(url, headers=headers, json=data)
        self.log.info(f"PUT's status code: {r.status_code}")
        return r.status_code

    def players_playerid_notes(self, username='welly', notes='Who am i'):
        env = Url(self.env)
        url = env.url_players_playerid_notes(username)

        _, get_token = self.login()

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization': get_token['token'],
            'Connection': 'keep-alive',
            'Content-Length': '21',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'ae-boapi.stgdevops.site',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
        }

        data = {
            'notes': notes
        }

        r = self.s.put(url, headers=headers, json=data)
        self.log.info(f"Status code: {r.status_code}")
        return r.status_code

    def transactions_search(self, username='welly'):
        env = Url(self.env)
        url = env.url_transactions_search()

        _, get_token = self.login()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Authorization': get_token['token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': '*/*',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        data = {
            'limit': '25',
            'offset': '0',
            'sort': 'DESC',
            'sortcolumn': 'txntime',
            'toplayer': username,
            'txntypes': '5',
        }
        r = self.s.get(url, headers=headers, data=data)
        self.log.info(r.json())


if __name__ == '__main__':

    player = PlayerResource('stg')
    player.players_list_search()