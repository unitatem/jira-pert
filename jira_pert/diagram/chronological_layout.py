from typing import Dict, List

import numpy as np

from jira_pert.model.pert_graph import PertGraph, PertNode


class ChronologicalLayout(object):
    def __init__(self, model: PertGraph):
        self._graph: Dict[str, PertNode] = model.get_graph()
        self._gates: [[str]] = []
        self._positions: Dict[str, List] = dict()

    def get_layout(self) -> Dict[str, List]:
        self._assign_nodes_to_gates()
        self._calculate_layout_positions()
        return self._positions

    def _assign_nodes_to_gates(self):
        for key, node in self._graph.items():
            blocking_gate = self._find_last_blocking_dependency_gate(key)
            blocking_gate += 1
            gate = self._get_gate(blocking_gate)
            gate.append(key)

    def _find_last_blocking_dependency_gate(self, key) -> int:
        blocking_gate = -1
        for dependency_key in self._graph[key].dependencies:
            for idx, gate in enumerate(self._gates):
                try:
                    _ = gate.index(dependency_key)
                    if idx > blocking_gate:
                        blocking_gate = idx
                except ValueError:
                    pass
        return blocking_gate

    def _get_gate(self, idx: int) -> [str]:
        if not idx < len(self._gates):
            self._gates.append([])
        return self._gates[idx]

    def _calculate_layout_positions(self):
        gates_cnt = len(self._gates)
        pos_x = np.linspace(-1.0, 1.0, gates_cnt + 2)[1:-1]

        for idx_x, gate in enumerate(self._gates):
            nodes_cnt = len(gate)
            pos_y = np.linspace(-1.0, 1.0, nodes_cnt + 2)[1:-1]
            for idx_y, node in enumerate(gate):
                self._positions[node] = [pos_x[idx_x], pos_y[idx_y]]
