from typing import Dict

from jira_pert.jira_wrapper import JiraDataV2


class PertNode(object):
    def __init__(self, key: str, **kwargs):
        self.key = key
        self.summary = kwargs.get('summary', '')
        self.ticket_type = kwargs.get('ticket_type', 'Story')
        self.dependencies = kwargs.get('dependencies', [])


class PertGraph(object):
    def __init__(self, features: [JiraDataV2] = None):
        if features is None:
            features = []
        self._graph = dict()
        self._build(features)

    def get_nodes_cnt(self):
        return len(self._graph)

    def _build(self, features: [JiraDataV2]):
        for feature in features:
            self._add_node(key=feature.get_key(),
                           summary=feature.get_summary(),
                           ticket_type=feature.get_type(),
                           dependencies=feature.get_blocking_issues_keys())

    def _add_node(self, **kwargs):
        node = PertNode(**kwargs)
        self._graph[kwargs['key']] = node

    def get_graph(self) -> Dict[str, PertNode]:
        return self._graph

    def print(self):
        for issue, node in self._graph.items():
            print("({ticket_type}){issue} depends on: {dependencies}".format(issue=issue,
                                                                             ticket_type=node.ticket_type,
                                                                             dependencies=node.dependencies))
