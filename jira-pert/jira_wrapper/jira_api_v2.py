from jira import JIRA
from ..server_connection import server_connection


class JiraAPIv2(object):
    _jira = None

    def __init__(self):
        self._setup_connection()

    def _setup_connection(self):
        if self._jira is not None:
            return

        options = {'server': server_connection['server_https']}
        self._jira = JIRA(options=options,
                          basic_auth=(server_connection['email'], server_connection['api_token']))

    def get_issues_in_epic(self, epic_key: str) -> []:
        features = self._jira.search_issues("'Epic Link' = {epic_key} order by created ASC".format(epic_key=epic_key))
        return features