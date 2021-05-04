import requests
import time
from . import ims
from . import log
from config.user import User


class Base:

    s = requests.session()

    def __init__(self, env='stg'):
        self.env = env

    def ims_login_with_pwd(self, username, pwd):
        url = ims.url_login()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
        }

        data = {
            "userid": username,
            "password": pwd
        }

        r = self.s.post(url, headers=headers, json=data, verify=False)
        log(f'\nStatus: {r.status_code}, User: {username}\nIms login: {r.json()}')
        return r.status_code, r.json()

    def ims_login(self, username='wellyadmin', ):
        url = ims.url_login()

        user = User(username)
        username = user.username()
        pwd = user.pwd()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Referer': 'https://ae-bo.stgdevops.site/',
        }

        data = {
            "userid": username,
            "password": pwd
        }

        r = self.s.post(url, headers=headers, json=data, verify=False)
        log(f'\nStatus: {r.status_code}, User: {username}\nIms login: {r.json()}')
        return r.status_code, r.json()

    def start_and_end_time(self, start_m,
                                 start_d,
                                 end_m,
                                 end_d):
        strftimes = (time.strftime('%Y') + f'-{start_m}-{start_d} 00:00:00',
                     time.strftime('%Y') + f'-{end_m}-{end_d} 23:59:59')

        for strftime in strftimes:
            strptime = time.strptime(strftime, '%Y-%m-%d %H:%M:%S')
            if strftime == strftimes[0]:
                todays_start = time.mktime(strptime)
            else:
                todays_end = time.mktime(strptime)

        return str(int(todays_start))+'000', str(int(todays_end))+'999'

    def header(self, token):
        headers = {
                'accept': '*/*',
                'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': token['token'],
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://ae-bo.stgdevops.site',
                'referer': 'https://ae-bo.stgdevops.site/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/87.0.4280.88 Safari/537.36',}
        return headers

    def user_roles_setting(self, token):
        url = ims.url_user_roles_setting()
        headers = self.header(token)
        data = {
              "rolename": "Super Admin",
              "permissionlist": [
                {
                  "funcnames": "Player Stat,Deposit Top 10 Today,Deposit Top 10 All Time,Withdraw Last 7 Days,"
                               "Registered Member Last 7 Days,Player List,New Registrant List,Online Player List,"
                               "Failed Login List,Failed Registration List,VIP Setting,Tag Management,Transaction List,"
                               "Deposit List,Withdrawal List,Withdrawal Condition List,Transfer List,Bank Type Setting,"
                               "Collection Account Setting,3rd Party Payment Platform,Manual Adjustment,Finance Setting,"
                               "Promotion Rule List,Promotion Request List,Rebate Setting,Pending Rebate List,Rebate History,"
                               "Rebate Stats,New Rebate Setting,New Pending Rebate List,New Rebate History,New Rebate Stats,"
                               "Announcement/News List,Advertisement List,Inbox Message,Static Page Setting,Template Setting,"
                               "Right Side Shortcut Setting,Overall Report,Turnover Record,Betting Histories,Player's Report,"
                               "Game Report,Promotion Report,P/L Report,Dfnn Report,Telephone Interview Report,Affiliate List,"
                               "Affiliate Referral Setting,Affiliate Referral Request,Affiliate Settlement List,"
                               "Affiliate Statistics,Master List,Agent List,Agent Register List,GGR List,"
                               "Settlement List,Agent Txn List,Agent Report,Agent Domain Setting,Group List,"
                               "Group Report,Group Settlement Report,Group Point Record,Group Request List,"
                               "Group Adjustment,Group Permission,Group Domain Setting,Admin Management,"
                               "Admin Role Management,Admin Log,Game API Setting,Product Maintenance,Provider List,"
                               "Product Type,Game Group,FE Game Table,Sports Valid Bets,Currency List,SMS Config,"
                               "IP Rules,Same IP/FP List,SexyLine Overall Report,SexyLine Binding Management",
                  "permission": 4
                },
                {
                  "funcnames": "Risk Control",
                  "permission": 1
                },
                {
                  "funcnames": "Share Site Setting,Notification History",
                  "permission": 2
                }
              ],
              "availableOperationsForRole": [
                "PLAYER_STATUS_UPDATE",
                "PLAYER_FORCED_LOGOUT",
                "PLAYER_ADD",
                "PLAYER_COMMENTS_ADD",
                "PLAYER_PASSWORD_RESET",
                "PLAYER_ALL_GAME_REGISTER",
                "PLAYER_TAG_EDIT",
                "PLAYER_VIP_UPDATE",
                "PLAYER_PERSONAL_INFO_EDIT",
                "PLAYER_WALLET_TRANSFER",
                "PLAYER_WITHDRAW_CONDITION_AUDIT",
                "PLAYER_BANKCARD_ADD",
                "PLAYER_BANKCARD_EDIT",
                "PLAYER_ACTIVE_BANKCARD_SUSPEND"
              ],
              "maskFieldsForRole": []}
        r = self.s.put(url, headers=headers, json=data)
        log(f"User roles setting's status code: {r.status_code}")
        if r.status_code != 204:
            raise ValueError('User roles setting failed.')

