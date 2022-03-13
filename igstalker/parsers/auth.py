import re

import requests


class AuthParser(object):

    def __init__(
        self,
        login_get_resp: requests.Response,
        login_post_resp: requests.Response
    ) -> None:
        self.login_get_resp = login_get_resp
        self.login_post_resp = login_post_resp
        pass

    def parse_sessionid(
        self
    ) -> str:
        pattern = '.*sessionid=([^;]+)'
        set_cookie = self.login_post_resp.headers['Set-Cookie']
        re_search = re.search(
            pattern=pattern,
            string=set_cookie
        )
        sessionid = re_search.group(1)
        return sessionid
