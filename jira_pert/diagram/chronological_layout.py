from typing import Dict, List

import numpy as np

from jira_pert.model.detect_cycle_dfs import DetectCycleDFS
from jira_pert.model.pert_graph import PertGraph, PertNode


class ChronologicalLayout(object):
    def __init__(self, model: PertGraph):
        self._graph: Dict[str, PertNode] = model.get_graph()
        self._gates: [[str]] = []
        self._positions: Dict[str, List[float]] = dict()

        detect_cycle = DetectCycleDFS(model)
        if detect_cycle.is_cyclic():
            raise ValueError('Graph has cycle', detect_cycle.get_cycle())

    def get_layout(self) -> Dict[str, List]:
        self._assign_nodes_to_gates()
        self._calculate_layout_positions()
        return self._positions

    def _assign_nodes_to_gates(self):
        keys = list(self._graph.keys())
        for key in keys:
            success = self._evaluate_key_dependencies_completeness(key)
            # retry later if not all dependencies can be located right now
            if not success:
                keys.append(key)

    def _evaluate_key_dependencies_completeness(self, key) -> bool:
        blocking_gate = -1
        for dependency_key in self._graph[key].dependencies:
            found = False
            for gate_idx, gate in enumerate(self._gates):
                try:
                    _ = gate.index(dependency_key)
                    # exception will be thrown if key does not exist
                    found = True
                    if gate_idx > blocking_gate:
                        blocking_gate = gate_idx
                    continue
                except ValueError:
                    pass
            if not found:
                return False

        self._add_key_to_gate(key, blocking_gate + 1)
        return True

    def _add_key_to_gate(self, key: str, gate_idx: int):
        if not gate_idx < len(self._gates):
            self._gates.append([])
        self._gates[gate_idx].append(key)

    def _calculate_layout_positions(self):
        gates_cnt = len(self._gates)
        pos_x = np.linspace(-1.0, 1.0, gates_cnt + 2)[1:-1]

        for idx_x, gate in enumerate(self._gates):
            nodes_cnt = len(gate)
            pos_y = np.linspace(-1.0, 1.0, nodes_cnt + 2)[1:-1]
            for idx_y, key in enumerate(gate):
                self._positions[key] = [pos_x[idx_x], pos_y[idx_y]]
