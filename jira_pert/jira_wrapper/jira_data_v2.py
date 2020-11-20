from jira.resources import Issue


class JiraDataV2(object):
    def __init__(self, issue: Issue):
        self._issue = issue

    def get_key(self) -> str:
        return self._issue.key

    def get_summary(self) -> str:
        return self._issue.raw['fields']['summary']

    def get_type(self) -> str:
        return self._issue.raw['fields']['issuetype']['name']

    def get_blocking_issues_keys(self) -> [str]:
        links = self._issue.raw['fields']['issuelinks']

        keys = []
        for link in links:
            key = JiraDataV2._get_blocking_keys(link)
            if len(key):
                keys += key
        return keys

    @staticmethod
    def _get_blocking_keys(link) -> [str]:
        issues_link_type = link['type']['name']
        if issues_link_type != 'Blocks':
            return []

        if 'inwardIssue' not in link:
            return []

        key = link['inwardIssue']['key']
        return [key]
