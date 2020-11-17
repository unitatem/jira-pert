from jira_pert.jira_wrapper import JiraAPIv2
from jira_pert.diagram.pert_diagram import PertDiagram
from jira_pert.model.pert_graph import PertGraph


def main():
    print('jira_pert is running...\n')

    epic_key = 'SAN-1'

    jira_api = JiraAPIv2()
    features = jira_api.get_issues_in_epic(epic_key)

    graph = PertGraph(features)
    graph.print()

    diagram = PertDiagram(graph)
    diagram.plot()


if __name__ == "__main__":
    main()
