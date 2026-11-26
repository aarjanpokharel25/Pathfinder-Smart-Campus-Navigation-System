"""Unit-test starter cases for the campus graph."""

import unittest

from core.graph import Graph
from core.location import Location
from core.path import Path


class TestGraph(unittest.TestCase):
    """Tests for graph location and path management."""

    def setUp(self) -> None:
        """Create a small graph for each test."""
        # TODO: Create locations and paths shared by graph tests.
        self.graph = Graph()

    def test_add_location(self) -> None:
        """Adding a location makes it available in the graph."""
        # TODO: Assert that a new location is stored.
        self.skipTest("TODO: Implement Graph.add_location before enabling.")

    def test_add_and_remove_path(self) -> None:
        """Paths can be added to and removed from the adjacency list."""
        # TODO: Assert that both directions of an undirected path change.
        self.skipTest("TODO: Implement Graph path methods before enabling.")

    def test_graph_starts_empty(self) -> None:
        """A new graph has empty location and adjacency dictionaries."""
        self.assertEqual(self.graph.locations, {})
        self.assertEqual(self.graph.adjacency_list, {})

    def test_location_and_path_models(self) -> None:
        """Location and path models retain their supplied values."""
        location = Location("library", "Library", 10.0, 20.0)
        path = Path("library", "gate", 12.5, blocked=True)

        self.assertEqual((location.location_id, location.name), ("library", "Library"))
        self.assertEqual((location.x, location.y), (10.0, 20.0))
        self.assertEqual((path.start_id, path.end_id), ("library", "gate"))
        self.assertEqual(path.distance, 12.5)
        self.assertTrue(path.blocked)


if __name__ == "__main__":
    unittest.main()
