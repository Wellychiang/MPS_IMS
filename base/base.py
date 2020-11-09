import logging
import sys
import requests
from config.url import Url


class Base:

    s = requests.session()
    log_path = './log/log.log'

    def __init__(self, env):

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

        console_log = logging.StreamHandler()  # sys.stdout
        logger.addHandler(console_log)

        file_handler = logging.FileHandler(self.log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        self.log = logger
        self.env = env

    def login(self, username='wellyadmin', pwd='64e89cab6f9b5560931d87399d916faf08e95c49'):
        site = Url(self.env)
        url = site.url_login()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            # 'Content-Length': '77',
            # 'Authorization': 'undefined',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            #               'Chrome/86.0.4240.111 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            # 'Accept': '*/*',
            'Origin': 'https://ae-bo.stgdevops.site',
            # 'Sec-Fetch-Site': 'same-site',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ae-bo.stgdevops.site/',
            # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            "userid": username,
            "password": pwd
        }

        r = self.s.post(url, headers=headers, json=data, verify=False)
        self.log.info(f'\nstatus: {r.status_code}\nresponse: {r.json()}')
        return r.status_code, r.json()

