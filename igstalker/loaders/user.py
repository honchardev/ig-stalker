import requests


class UserLoader(object):
    urls = {
        'get': {
            'userpage': 'https://www.instagram.com/{0}/'
        }
    }

    def __init__(
        self,
        user_agent: str,
        session: requests.Session
    ) -> None:
        self.user_agent = user_agent
        self.session = session

    def userpage_get(
        self,
        username: str
    ) -> requests.Response:
        url = self.urls['get']['userpage'].format(username)
        resp = self.session.get(url)
        return resp
