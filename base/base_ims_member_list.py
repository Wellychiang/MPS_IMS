from base.base import Base
from . import ims
from . import log


# 會員列表
class MemberList(Base):

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
        
        url = ims.url_players_list_search()

        _, get_token = self.ims_login()
        headers = self.header(get_token)

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
        log(f'Player list search: {str(r.json()).encode("utf-8").decode("cp950", "ignore")}')

        return r.status_code, r.json()

    def players_list_lookup(self, username='welly'):
        
        url = ims.url_players_list_lookup()

        _, get_token = self.ims_login()
        headers = self.header(get_token)

        params = {
            'q': username
        }

        r = self.s.get(url, headers=headers, params=params)
        log(f'Look up: {r.json()}')
        return r.status_code, r.json()

    def add_player(self, username='welly', user_num=''):
        
        url = ims.url_add_player()

        _, get_token = self.ims_login()
        headers = self.header(get_token)

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
        log(f'Add_player: {r.json()}')
        return r.status_code, r.json()

    def players_playerid(self, username='welly'):
        
        url = ims.url_players_playerid(username)

        _, get_token = self.ims_login()
        headers = self.header(get_token)

        r = self.s.get(url, headers=headers)
        log(f'Players playerid: {r.json()}')

        return r.status_code, r.json()

    def players_playerid_status(self, username='welly', status=1):
        
        url = ims.url_players_playerid_status(username)

        _, get_token = self.ims_login()

        headers = self.header(get_token)
        data = {
            'status': status
        }

        r = self.s.put(url, headers=headers, json=data)
        log(f"PUT's status code: {r.status_code}")
        return r.status_code

    def players_playerid_notes(self, username='welly', notes=None, method='put'):
        
        url = ims.url_players_playerid_notes(username)

        _, get_token = self.ims_login()
        headers = self.header(get_token)

        if method == 'get':
            headers.pop('Content-Type')

            data = {
                'limit': 16,
                'offset': 0,
                'sort': 'DESC',
                'sortcolumn': 'createdate'
            }

            r = self.s.get(url, headers=headers, params=data)
            log(f"Player's note status code: {r.status_code}")

            return r.status_code, r.json()

        elif method == 'put':
            data = {
                'notes': notes
            }

            r = self.s.put(url, headers=headers, json=data)
            log(f"Player's note status code: {r.status_code}")

            return r.status_code

    # 有重複的key: txntypes=5是手動加錢狀態, =6是扣錢狀態, 重複出現的話會顯示錯誤response
    def transactions_search(self, username='welly',
                            endtxnamt=None,
                            endtxntime=None,
                            starttxntime=None,
                            limit='25',
                            offset=0,
                            sort='DESC',
                            sortcolumn='txntime',
                            starttxnamt=None,
                            txntypes=5):
        
        url = ims.url_transactions_search()

        _, get_token = self.ims_login()
        headers = self.header(get_token)

        params = {
            'endtxnamt': endtxnamt,
            'endtxntime': endtxntime,
            'limit': limit,
            'offset': offset,
            'sort': sort,
            'sortcolumn': sortcolumn,
            'starttxnamt': starttxnamt,
            'starttxntime': starttxntime,
            'toplayer': username,
            'txntypes': txntypes,
            # 'txntypes': '6',
        }
        r = self.s.get(url, headers=headers, params=params)
        log(f'Transaction search: {r.json()}')
        return r.status_code, r.json()

    # 人工餘額調整txntypes=5是手動加錢, 6是扣錢
    def player_wallets(self, username='welly',
                       remarks='qq',
                       txnamt=100,
                       txntype='5'):
        
        url = ims.url_player_wallets()

        _, get_token = self.ims_login()
        headers = self.header(get_token)

        data = {
            'remarks': remarks,
            'toplayer': username,
            'txnamt': txnamt,
            'txntype': txntype,   # 5是加錢, 6是扣
        }
        r = self.s.put(url, headers=headers, json=data)
        log(f'Players wallets: {r.status_code}')
        return r.status_code
