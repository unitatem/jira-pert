from jira import JIRA
from .server_connection import server_connection


def main():
    print('jira-pert is running...\n')

    options = {'server': server_connection['server_https']}
    jira = JIRA(options=options,
                basic_auth=(server_connection['email'], server_connection['api_token']))

    projects = jira.projects()
    print(projects)


if __name__ == "__main__":
    main()
