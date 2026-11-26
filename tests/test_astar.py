"""Unit-test starter cases for A* search."""

import unittest

from algorithms.astar import AStar
from core.graph import Graph


class TestAStar(unittest.TestCase):
    """Tests for A* route search."""

    def setUp(self) -> None:
        """Create a graph with coordinates and a known shortest route."""
        # TODO: Build a small weighted graph with coordinate-aware locations.
        self.graph = Graph()
        self.algorithm = AStar()

    def test_finds_shortest_path(self) -> None:
        """The result includes the shortest route and its measurements."""
        # TODO: Verify path, distance, nodes explored, and execution time.
        self.skipTest("TODO: Implement AStar.find_path before enabling.")

    def test_heuristic_uses_euclidean_distance(self) -> None:
        """The heuristic estimates straight-line distance between locations."""
        # TODO: Check the result for a simple coordinate pair.
        self.skipTest("TODO: Implement AStar._heuristic before enabling.")


if __name__ == "__main__":
    unittest.main()
