import matplotlib.pyplot as plt
import networkx as nx

from jira_pert.pert_graph import PertGraph


class PertDiagram(object):
    def __init__(self, graph: PertGraph):
        self._model = graph

    def plot(self):
        graph = nx.DiGraph()

        for key, node in self._model.get_graph().items():
            graph.add_node(key)
            for dependency in node.dependencies:
                graph.add_edge(dependency, key)

        self._draw(graph)

    def _draw(self, graph):
        # nx.draw_networkx()
        # nx.draw_networkx_edges()
        nx.draw(graph,
                pos=nx.spectral_layout(graph),
                with_labels=True,
                **self._get_node_style())
        plt.show()

    @staticmethod
    def _get_node_style():
        return dict(
            node_size=2200,
            node_color='blue',
            edgecolors='blue',
            bbox=dict(
                facecolor='white',
                edgecolor='blue',
                boxstyle='round,pad=0.5')
        )
