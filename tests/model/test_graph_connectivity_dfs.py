import unittest

from jira_pert.model.graph_connectivity_dfs import GraphConnectivityDFS
from jira_pert.model.pert_graph import PertGraph


class MyTestCase(unittest.TestCase):
    def test_connected_graph(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=[])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['A'])

        graph_connectivity = GraphConnectivityDFS(graph)
        self.assertEqual(True, graph_connectivity.is_connected())

    def test_not_connected_graph(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=[])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=[])

        graph_connectivity = GraphConnectivityDFS(graph)
        self.assertEqual(False, graph_connectivity.is_connected())


if __name__ == '__main__':
    unittest.main()
