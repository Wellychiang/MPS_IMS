import logging
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


