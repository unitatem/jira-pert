import optparse

from jira_pert.jira_wrapper import JiraAPIv2
from jira_pert.diagram.pert_diagram import PertDiagram
from jira_pert.model.pert_graph import PertGraph


def parse_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-k', '--key',
                      action="store", dest="key",
                      help="Jira story ID", default="SAN-1")

    options, args = parser.parse_args()
    return options


def main():
    print('jira_pert is running...\n')
    options = parse_arguments()

    epic_key = options.key

    jira_api = JiraAPIv2()
    features = jira_api.get_issues_in_epic(epic_key)

    graph = PertGraph(features)
    graph.print()

    diagram = PertDiagram(graph)
    diagram.plot()


if __name__ == "__main__":
    main()
