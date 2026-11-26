"""Weighted adjacency-list graph for the campus map."""

from typing import Dict, List, Tuple

from core.location import Location
from core.path import Path


class Graph:
    """Store campus locations and their weighted path connections."""

    def __init__(self) -> None:
        """Initialize empty location and adjacency dictionaries."""
        self.locations: Dict[str, Location] = {}
        self.adjacency_list: Dict[str, Dict[str, Path]] = {}

    def add_location(self, location: Location) -> None:
        """Add a location to the graph."""
        # TODO: Add the location and initialize its adjacency entry.
        raise NotImplementedError

    def remove_location(self, location_id: str) -> None:
        """Remove a location and all paths connected to it."""
        # TODO: Remove this vertex and references to it from other vertices.
        raise NotImplementedError

    def add_path(self, path: Path) -> None:
        """Add a weighted path to the adjacency list."""
        # TODO: Add the path in both directions for this undirected map.
        raise NotImplementedError

    def remove_path(self, start_id: str, end_id: str) -> None:
        """Remove the path between two locations."""
        # TODO: Remove both adjacency entries for this undirected path.
        raise NotImplementedError

    def get_neighbors(self, location_id: str) -> List[Tuple[Location, Path]]:
        """Return the neighboring locations and paths for a location."""
        # TODO: Return each available neighbor together with its Path.
        raise NotImplementedError

    def set_path_blocked(
        self, start_id: str, end_id: str, blocked: bool
    ) -> None:
        """Block or unblock a path between two locations."""
        # TODO: Update the shared path's blocked state.
        raise NotImplementedError
