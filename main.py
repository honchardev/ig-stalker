import random
from igstalker import Auth, Stalker


def get_creds(
    creds_filepath: str
) -> tuple:
    with open(creds_filepath) as fs_r:
        content = fs_r.readlines()
        return content[0], content[1]


def get_user_agent(
    user_agents_filepath: str
) -> str:
    with open(user_agents_filepath) as fs_r:
        content = fs_r.readlines()
        return random.choice(content)


def main():
    creds_filepath = 'assets/creds/acc2.txt'
    stalker_username, stalker_password = get_creds(creds_filepath)

    user_agents_filepath = 'assets/user_agents.txt'
    user_agent = get_user_agent(user_agents_filepath)

    auth = Auth(user_agent, stalker_username, stalker_password)
    session = auth.login()

    stalker = Stalker(session)
    stories = stalker.get_stories()

    print(stories)


if __name__ == '__main__':
    main()
