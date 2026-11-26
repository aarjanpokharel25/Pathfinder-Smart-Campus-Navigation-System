"""Unit-test starter cases for Dijkstra's algorithm."""

import unittest

from algorithms.dijkstra import Dijkstra
from core.graph import Graph


class TestDijkstra(unittest.TestCase):
    """Tests for Dijkstra route search."""

    def setUp(self) -> None:
        """Create a graph with a known shortest route."""
        # TODO: Build a small weighted graph with multiple possible routes.
        self.graph = Graph()
        self.algorithm = Dijkstra()

    def test_finds_shortest_path(self) -> None:
        """The result includes the shortest route and its measurements."""
        # TODO: Verify path, distance, nodes explored, and execution time.
        self.skipTest("TODO: Implement Dijkstra.find_path before enabling.")

    def test_ignores_blocked_path(self) -> None:
        """Blocked paths are not included in the search."""
        # TODO: Block an edge and verify the returned route avoids it.
        self.skipTest("TODO: Implement Dijkstra.find_path before enabling.")


if __name__ == "__main__":
    unittest.main()
