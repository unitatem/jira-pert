from .pert_graph import PertGraph
import matplotlib.pyplot as plt
import networkx as nx


class PertDiagram(object):
    def __init__(self, graph: PertGraph):
        self._model = graph

    def plot(self):
        self._model.print()

        graph = nx.DiGraph()
        for key, node in self._model.get_graph().items():
            graph.add_node(key)
            for dependency in node.dependencies:
                graph.add_edge(dependency, key)

        nx.draw(graph, with_labels=True)
        plt.show()
