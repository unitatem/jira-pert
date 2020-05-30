from .jira_wrapper import JiraAPIv2
from .jira_wrapper import JiraDataV2


def main():
    print('jira-pert is running...\n')
    jira_api = JiraAPIv2()

    epic_key = 'SAN-1'
    features = jira_api.get_issues_in_epic(epic_key)
    for feature in features:
        print(JiraDataV2.get_key(feature))
        print("depends on:", JiraDataV2.get_blocking_issues_keys(feature))


if __name__ == "__main__":
    main()
