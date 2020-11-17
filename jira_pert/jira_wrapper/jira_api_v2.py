from jira import JIRA

from .connection_configuration import ConnectionConfiguration
from .jira_data_v2 import JiraDataV2


class JiraAPIv2(object):
    _jira = None

    def __init__(self):
        self._setup_connection()

    def _setup_connection(self):
        if self._jira is not None:
            return

        config = ConnectionConfiguration()
        options = {'server': config.server_https}
        self._jira = JIRA(options=options,
                          basic_auth=(config.email, config.api_token))

    def get_issues_in_epic(self, epic_key: str) -> [JiraDataV2]:
        issues_raw = self._jira.search_issues("'Epic Link' = {epic_key} order by created ASC".format(epic_key=epic_key))
        issues = [JiraDataV2(f) for f in issues_raw]
        return issues
