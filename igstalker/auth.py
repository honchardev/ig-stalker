import requests

from igstalker.loaders.auth import AuthLoader
from igstalker.parsers.auth import AuthParser
from igstalker.utils.auth import AuthUtils


class Auth(object):

    def __init__(
        self,
        user_agent: str,
        stalker_username: str,
        stalker_password: str
    ):
        self.creds = {
            'username': stalker_username,
            'password': stalker_password
        }
        self.loader = AuthLoader(user_agent)
        self.parser = None
        self.utils = AuthUtils()

    def login(
        self
    ) -> requests.Session:
        login_get = self.loader.login_get()

        enc_password = self.utils.get_enc_password(self.creds['password'])
        login_post = self.loader.login_post(
            username=self.creds['username'],
            enc_password=enc_password,
            csrf_token=login_get.cookies['csrftoken']
        )

        self.parser = AuthParser(login_get, login_post)
        sessionid = self.parser.parse_sessionid()
        cookies = self.utils.get_session_cookie(sessionid)
        session = self.utils.get_session(cookies)

        return session
