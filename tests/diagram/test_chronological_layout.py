import unittest

from jira_pert.diagram.chronological_layout import ChronologicalLayout
from jira_pert.model.pert_graph import PertGraph


class ChronologicalLayoutTest(unittest.TestCase):
    def test_three_nodes_in_order(self):
        graph = PertGraph()
        graph._add_node('A', "", [])
        graph._add_node('B', "", ['A'])
        graph._add_node('C', "", ['B'])

        engine = ChronologicalLayout(graph)
        engine.get_layout()

        self.assertEqual(['A'], engine._gates[0])
        self.assertEqual(['B'], engine._gates[1])
        self.assertEqual(['C'], engine._gates[2])

    def test_three_nodes_in_reverse_order(self):
        graph = PertGraph()
        graph._add_node('C', "", ['B'])
        graph._add_node('B', "", ['A'])
        graph._add_node('A', "", [])

        engine = ChronologicalLayout(graph)
        engine.get_layout()

        self.assertEqual(['A'], engine._gates[0])
        self.assertEqual(['B'], engine._gates[1])
        self.assertEqual(['C'], engine._gates[2])


if __name__ == '__main__':
    unittest.main()
