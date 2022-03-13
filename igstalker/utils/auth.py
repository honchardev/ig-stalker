import datetime

import requests


class AuthUtils(object):

    @staticmethod
    def get_enc_password(
        password: str
    ) -> str:
        version = 0
        now_timestamp = datetime.datetime.now().timestamp()
        enc_password = f'#PWD_INSTAGRAM_BROWSER:{version}:{now_timestamp:.0f}:{password}'
        return enc_password

    @staticmethod
    def get_session_cookie(
        sessionid: str
    ) -> dict:
        cookie = requests.cookies.create_cookie(
            name='sessionid',
            secure=True,
            value=sessionid
        )
        return cookie

    @staticmethod
    def get_session(
        cookies: dict
    ) -> requests.Session:
        session = requests.session()
        session.cookies.set_cookie(cookies)
        return session
