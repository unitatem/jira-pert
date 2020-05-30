class PERTNode(object):
    def __init__(self, key: str, summary: str, dependencies: [str]):
        self.key = key
        self.summary = summary
        self.dependencies = dependencies


class PertGraph(object):
    def __init__(self):
        self._graph = dict()

    def add_node(self, issue_key: str, summary: str, dependencies: [str]):
        node = PERTNode(issue_key, summary, dependencies)
        self._graph[issue_key] = node

    def print(self):
        for issue, node in self._graph.items():
            print("{issue} depends on: {dependencies}".format(issue=issue,
                                                              dependencies=node.dependencies))
