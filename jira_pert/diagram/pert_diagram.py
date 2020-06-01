from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx

from jira_pert.diagram.chronological_layout import ChronologicalLayout
from jira_pert.model.pert_graph import PertGraph


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

    def _draw(self, graph: nx.DiGraph):
        # nx.draw_networkx()
        # nx.draw_networkx_edges()
        nx.draw(graph,
                **self._get_labels(),
                **self._get_layout(graph),
                **self._get_node_style())
        plt.show()

    def _get_labels(self) -> Dict:
        labels = dict()
        for key, node in self._model.get_graph().items():
            labels[key] = node.summary

        return dict(
            with_labels=True,
            labels=labels
        )

    def _get_layout(self, graph) -> Dict:
        # default: pos=nx.spectral_layout(graph)
        return dict(
            pos=ChronologicalLayout(self._model).get_layout()
        )

    @staticmethod
    def _get_node_style() -> Dict:
        return dict(
            node_size=2200,
            node_color='blue',
            edgecolors='blue',
            bbox=dict(
                facecolor='white',
                edgecolor='blue',
                boxstyle='round,pad=0.5')
        )
