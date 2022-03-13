import requests


class AuthLoader(object):
    urls = {
        'get': {
            'login': 'https://www.instagram.com/accounts/login/'
        },
        'post': {
            'login': 'https://www.instagram.com/accounts/login/ajax/'
        }
    }

    def __init__(
        self,
        user_agent: str
    ) -> None:
        self.user_agent = user_agent

    def login_get(
        self
    ) -> requests.Response:
        url = self.urls['get']['login']
        resp = requests.get(url)
        return resp

    def login_post(
        self,
        username: str,
        enc_password: str,
        csrf_token: str
    ) -> requests.Response:
        url = self.urls['post']['login']
        data = {
            'enc_password': enc_password,
            'optIntoOneTap': 'false',
            'queryParams': {},
            'username': username,
        }
        header = {
            'referer': self.urls['get']['login'],
            'user-agent': self.user_agent,
            'x-csrftoken': csrf_token,
            'x-requested-with': 'XMLHttpRequest',
        }
        resp = requests.post(
            url=url,
            data=data,
            headers=header
        )
        return resp
