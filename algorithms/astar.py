"""A* shortest-path search with a Euclidean distance heuristic."""

import heapq
import math
import time
from typing import List, Tuple

from core.graph import Graph
from core.location import Location


class AStar:
    """Find a shortest route using A* search."""

    def _heuristic(self, location: Location, goal: Location) -> float:
        """Estimate distance between locations using Euclidean distance."""
        # TODO: Calculate the straight-line distance from their coordinates.
        raise NotImplementedError

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
        # TODO: Use heapq, the Euclidean heuristic, and time.perf_counter().
        # Skip blocked paths and count explored nodes.
        raise NotImplementedError
