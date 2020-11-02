import sys
sys.path.append('..')

from base import logger, Base
from config.url import Url


class AdResource(Base):

    def ad(self):
        env = Url(self.env)
        url = env.url_ads()

        ad = AdResource(self.env)
        _, get_token = ad.login()

        headers = {
            'Host': 'ae-boapi.stgdevops.site',
            'Connection': 'keep-alive',
            'Content-Length': '1305508',
            'Authorization': get_token['token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary1qegbUo2O4OtJU84',
            'Accept': '*/*',
            'Origin': 'https://ae-bo.stgdevops.site',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ae-bo.stgdevops.site/',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {

        }

    def test(self):
        self.login()


if __name__ == '__main__':
    a = AdResource('stg')
    a.test()
    # self.login()
