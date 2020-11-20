from typing import Dict

import matplotlib.pyplot as plt
import networkx as nx

from jira_pert.diagram.chronological_layout import ChronologicalLayout
from jira_pert.diagram.diagram_config import DiagramConfig
from jira_pert.model.pert_graph import PertGraph


class PertDiagram(object):
    def __init__(self, model: PertGraph):
        self._model = model
        self._graph: nx.DiGraph = None
        self._config = DiagramConfig()

    def plot(self):
        self._graph = nx.DiGraph()

        for key, node in self._model.get_graph().items():
            self._graph.add_node(key)
            for dependency in node.dependencies:
                self._graph.add_edge(dependency, key)

        self._draw()

    def _draw(self):
        # nx.draw_networkx()
        # nx.draw_networkx_edges()
        nx.draw(self._graph,
                **self._get_labels(),
                **self._get_layout(self._graph),
                **self._get_node_style())
        plt.show()

    def _get_labels(self) -> Dict:
        labels = dict()
        for key, node in self._model.get_graph().items():
            labels[key] = node.key

        return dict(
            with_labels=True,
            labels=labels
        )

    def _get_layout(self, graph) -> Dict:
        # default: pos=nx.spectral_layout(graph)
        return dict(
            pos=ChronologicalLayout(self._model).get_layout()
        )

    def _get_node_style(self) -> Dict:
        return dict(
            node_size=2200,
            node_color=self._get_node_colors(),
            edgecolors='blue',
            bbox=dict(
                facecolor='white',
                edgecolor='blue',
                boxstyle='round,pad=0.5')
        )

    def _get_node_colors(self) -> [str]:
        node_colors = []
        for node in self._graph:
            ticket_type = self._model.get_graph()[node].ticket_type
            color = self._config.config['node_color'][ticket_type]
            node_colors.append(color)
        return node_colors
