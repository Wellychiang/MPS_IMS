import sys
sys.path.append('..')
from base.base import Base
from config.url import Url


class PlayerResource(Base):

    def players_list_search(self, language='2', limit='25', loginend='-1', loginstart='-1', offset='0',
                            playerid='welly', playeridexactmatch='False', sort='ASC'):
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
            'language': language,  # int, default value: 2
            'limit': limit,  # int, default value: 25
            'loginend': loginend,  # int, default value: -1
            'loginstart': loginstart,  # int, default value: -1
            'offset': offset,  # int, default value: 0
            'playerid': playerid,  # String
            # Boolean
            'playeridexactmatch': playeridexactmatch,
            'sort': sort,  # (String)Default value : ASC, available: ASC, DESC

            # (String)Available values : playerid, firstname, viplevel, currency, createdate, city, agentid,
            # totalavailable, totaldeposit, totalwithdraw, logintime, status, totaldepositcount, totalwithdrawcount
            'sortcolumn': 'playerid'
        }

        r = self.s.get(url, headers=headers, params=params)
        self.log.info(str(r.json()).encode("utf-8").decode("cp950", "ignore"))
        return r.status_code, r.json()


if __name__ == '__main__':

    player = PlayerResource('stg')
    player.players_list_search()