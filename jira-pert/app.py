from .jira_wrapper import JiraAPIv2
from .jira_wrapper import JiraDataV2
from .pert_graph import PertGraph
from .pert_diagram import PertDiagram


def main():
    print('jira-pert is running...\n')

    epic_key = 'SAN-1'

    jira_api = JiraAPIv2()
    features = jira_api.get_issues_in_epic(epic_key)

    graph = PertGraph()
    for feature in features:
        graph.add_node(issue_key=JiraDataV2.get_key(feature),
                       summary=JiraDataV2.get_summary(feature),
                       dependencies=JiraDataV2.get_blocking_issues_keys(feature))

    diagram = PertDiagram(graph)
    diagram.plot()


if __name__ == "__main__":
    main()
