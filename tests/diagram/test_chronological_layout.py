import unittest

from jira_pert.diagram.chronological_layout import ChronologicalLayout
from jira_pert.model.pert_graph import PertGraph


class ChronologicalLayoutTest(unittest.TestCase):
    def test_three_nodes_in_order(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=[])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['B'])

        engine = ChronologicalLayout(graph)
        engine.get_layout()

        self.assertEqual(['A'], engine._gates[0])
        self.assertEqual(['B'], engine._gates[1])
        self.assertEqual(['C'], engine._gates[2])

    def test_three_nodes_in_reverse_order(self):
        graph = PertGraph()
        graph._add_node(key='C', dependencies=['B'])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='A', dependencies=[])

        engine = ChronologicalLayout(graph)
        engine.get_layout()

        self.assertEqual(['A'], engine._gates[0])
        self.assertEqual(['B'], engine._gates[1])
        self.assertEqual(['C'], engine._gates[2])

    def test_graph_with_cycle(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=['C'])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['B'])

        self.assertRaises(ValueError, ChronologicalLayout, graph)


if __name__ == '__main__':
    unittest.main()
