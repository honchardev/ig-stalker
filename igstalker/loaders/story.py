import json
import urllib.parse

import requests


class StoryLoader(object):
    urls = {
        'get': {
            'api': 'https://i.instagram.com/api/v1/feed/user/{0}/story/',
            'graphql': 'https://www.instagram.com/graphql/query/{0}',
        }
    }

    def __init__(
        self,
        user_agent: str,
        session: requests.Session
    ) -> None:
        self.user_agent = user_agent
        self.session = session

    def api_get(
        self,
        user_id: str
    ) -> requests.Response:
        url = self.urls['get']['api'].format(user_id)
        resp = self.session.get(url)
        return resp

    def graphql_get(
        self,
        user_id: str
    ) -> requests.Response:
        graphql_variables = {
            "reel_ids": [user_id],
            "tag_names": [],
            "location_ids": [],
            "highlight_reel_ids": [],
            "precomposed_overlay": False,
            "show_story_viewer_list": True,
            "story_viewer_fetch_count": 50,
            "story_viewer_cursor": "",
            "stories_video_dash_manifest": False
        }
        graphql_variables_str = json.dumps(
            graphql_variables, separators=(',', ':')
        )
        urlenc_graphql_variables_str = urllib.parse.quote(
            graphql_variables_str
        )
        url_variables = {
            'query_hash': 'c9c56db64beb4c9dea2d17740d0259d9',
            'variables': urlenc_graphql_variables_str
        }
        url_variables_str = '?' + '&'.join([
            f'{name}={value}'
            for name, value in url_variables.items()
        ])
        url = self.urls['get']['graphql'].format(url_variables_str)
        resp = self.session.get(url)
        return resp
