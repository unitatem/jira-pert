from jira.resources import Issue


class JiraDataV2(object):
    @staticmethod
    def get_key(issue: Issue) -> str:
        return issue.key

    @staticmethod
    def get_blocking_issues_keys(issue: Issue) -> [str]:
        links = issue.raw['fields']['issuelinks']

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
