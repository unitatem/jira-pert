from jira_pert.model.pert_graph import PertGraph


class DetectCycleDFS(object):
    def __init__(self, graph: PertGraph):
        self._graph = graph
        self._cycle = []

    def is_cyclic(self):
        self._cycle = []

        visited = dict()
        recursion_stack = dict()
        for key in self._graph.get_graph().keys():
            visited[key] = False
            recursion_stack[key] = False

        for key in self._graph.get_graph().keys():
            if self._is_cyclic(key, visited, recursion_stack):
                self._cycle.append(key)
                return True
        return False

    def _is_cyclic(self, key, visited, recursion_stack):
        if not visited[key]:
            visited[key] = True
            recursion_stack[key] = True

            for dependency_key in self._graph.get_graph()[key].dependencies:
                if not visited[dependency_key] and self._is_cyclic(dependency_key, visited, recursion_stack):
                    self._cycle.append(dependency_key)
                    return True
                elif recursion_stack[dependency_key]:
                    self._cycle.append(dependency_key)
                    return True

        recursion_stack[key] = False
        return False

    def get_cycle(self):
        return self._cycle
