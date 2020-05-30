from .jira_wrapper import JiraAPIv2
from .jira_wrapper import JiraDataV2
from .pert_graph import PertGraph


def main():
    print('jira-pert is running...\n')
    jira_api = JiraAPIv2()

    epic_key = 'SAN-1'
    features = jira_api.get_issues_in_epic(epic_key)

    graph = PertGraph()
    for feature in features:
        graph.add_node(issue_key=JiraDataV2.get_key(feature),
                       summary=JiraDataV2.get_summary(feature),
                       dependencies=JiraDataV2.get_blocking_issues_keys(feature))
    graph.print()


if __name__ == "__main__":
    main()
