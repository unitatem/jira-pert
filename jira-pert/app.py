from jira import JIRA
from .server_connection import server_connection


def setup_connection():
    options = {'server': server_connection['server_https']}
    jira = JIRA(options=options,
                basic_auth=(server_connection['email'], server_connection['api_token']))
    return jira


def main():
    print('jira-pert is running...\n')
    jira = setup_connection()

    epic_key = 'MAR-36'
    features = jira.search_issues("'Epic Link' = {epic_key}".format(epic_key=epic_key))
    print(features)


if __name__ == "__main__":
    main()
