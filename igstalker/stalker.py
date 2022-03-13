import requests

from igstalker.loaders.story import StoryLoader
from igstalker.loaders.user import UserLoader
from igstalker.parsers.story import StoryParser
from igstalker.parsers.user import UserParser
from igstalker.utils.story import StoryUtils
from igstalker.utils.user import UserUtils


class Stalker(object):

    def __init__(
        self,
        user_agent: str,
        session: requests.Session,
    ) -> None:
        self.session = session
        self.user_handler = {
            'loader': UserLoader(user_agent, session),
            'parser': None,
            'utils': UserUtils(),
        }
        self.story_handler = {
            'loader': StoryLoader(user_agent, session),
            'parser': None,
            'utils': StoryUtils(),
        }

    def get_user(
        self,
        username: str
    ) -> dict:
        userpage_resp = self.user_handler['loader'].userpage_get(username)

        self.user_handler['parser'] = UserParser(userpage_resp)

        return self.user_handler['parser'].parse()

    def get_stories(
        self,
        username: str
    ) -> dict:
        if not self.user_handler['parser']:
            _ = self.get_user(username)

        user_id = self.user_handler['parser'].parse_user_id()
        story_resp = self.story_handler['loader'].graphql_get(user_id)

        self.story_handler['parser'] = StoryParser(story_resp)

        return self.story_handler['parser'].parse()
