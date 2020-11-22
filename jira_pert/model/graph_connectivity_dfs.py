from jira_pert.model.pert_graph import PertGraph


class GraphConnectivityDFS(object):
    def __init__(self, graph: PertGraph):
        self._adjacency_list = dict()
        self._build_undirected_graph(graph)

    def _build_undirected_graph(self, graph: PertGraph):
        for key in graph.get_graph().keys():
            self._adjacency_list[key] = []

        for key, node in graph.get_graph().items():
            for neighbour in node.dependencies:
                self._adjacency_list[key].append(neighbour)
                self._adjacency_list[neighbour].append(key)

    def is_connected(self):
        if len(self._adjacency_list) == 0:
            raise ValueError('Graph does not have nodes')

        visited = dict()
        for key in self._adjacency_list.keys():
            visited[key] = False

        self._is_connected(list(self._adjacency_list.keys())[0], visited)

        for _, node in visited.items():
            if not node:
                return False
        return True

    def _is_connected(self, key, visited):
        if not visited[key]:
            visited[key] = True

            for k in self._adjacency_list[key]:
                self._is_connected(k, visited)
