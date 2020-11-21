import unittest

from jira_pert.model.cycle_detector_dfs import CycleDetectorDFS
from jira_pert.model.pert_graph import PertGraph


class MyTestCase(unittest.TestCase):
    def test_non_cyclic_graph(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=[])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['A'])
        graph._add_node(key='D', dependencies=['B', 'C'])

        engine = CycleDetectorDFS(graph)
        self.assertEqual(False, engine.is_cyclic())

    def test_cyclic_graph_1(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=['C'])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['B'])

        engine = CycleDetectorDFS(graph)
        self.assertEqual(True, engine.is_cyclic())
        self.assertEqual(['A', 'B', 'C', 'A'], engine.get_cycle())

    def test_cyclic_graph_2(self):
        graph = PertGraph()
        graph._add_node(key='A', dependencies=[])
        graph._add_node(key='B', dependencies=['A'])
        graph._add_node(key='C', dependencies=['A', 'E'])
        graph._add_node(key='D', dependencies=['C'])
        graph._add_node(key='E', dependencies=['B', 'D'])

        engine = CycleDetectorDFS(graph)
        self.assertEqual(True, engine.is_cyclic())
        self.assertEqual(['C', 'D', 'E', 'C'], engine.get_cycle())


if __name__ == '__main__':
    unittest.main()
