import json

import requests
from bs4 import BeautifulSoup


class UserParser(object):

    def __init__(
        self,
        userpage_resp: requests.Response
    ) -> None:
        self.userpage_resp = userpage_resp
        self.userpage_bs = BeautifulSoup(
            markup=userpage_resp.text,
            features='html.parser'
        )

    def parse(
        self
    ) -> dict:
        return {}  # TODO: parsed User object

    def parse_user_id(
        self
    ) -> str:
        js_scripts = self.userpage_bs.find_all('script')

        js_script_with_userid = js_scripts[4].text

        js_script_sharedData_str = js_script_with_userid.replace(
            'window._sharedData = ',
            ''
        ).replace(
            '};',
            '}'
        )
        js_script_sharedData_dict = json.loads(js_script_sharedData_str)

        graphql_userid = js_script_sharedData_dict['entry_data']['ProfilePage'][0]['graphql']['user']['id']
        return graphql_userid
