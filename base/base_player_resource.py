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
                            im2=None):
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
            'offset': offset,                           # offset=1, 搜尋出來的任何比數資料都會少一筆
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
            'im2': im2                                  # 會進行客製化的咚咚(聯絡方式)
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


if __name__ == '__main__':

    player = PlayerResource('stg')
    player.players_list_search()