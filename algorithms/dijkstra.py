"""Dijkstra shortest-path search."""

import heapq
import time
from typing import List, Tuple

from core.graph import Graph


class Dijkstra:
    """Find a shortest route using Dijkstra's algorithm."""

    def find_path(
        self, graph: Graph, start_id: str, goal_id: str
    ) -> Tuple[List[str], float, int, float]:
        """Search for a shortest route in a weighted graph.

        Args:
            graph: Campus graph to search.
            start_id: Identifier of the starting location.
            goal_id: Identifier of the destination.

        Returns:
            A tuple of (path location IDs, total distance, nodes explored,
            execution time in seconds).
        """
        # TODO: Use heapq for the priority queue and time.perf_counter() to
        # measure the search. Skip blocked paths and count explored nodes.
        raise NotImplementedError
