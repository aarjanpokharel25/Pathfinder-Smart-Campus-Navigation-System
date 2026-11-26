"""JSON persistence for campus maps."""

import json
from pathlib import Path as FilePath
from typing import Union

from core.graph import Graph


class MapManager:
    """Load a campus graph from JSON and save it back to JSON."""

    def __init__(self, file_path: Union[str, FilePath]) -> None:
        """Create a manager for a campus map file."""
        self.file_path = FilePath(file_path)

    def load_map(self) -> Graph:
        """Load locations and paths from JSON into a Graph."""
        # TODO: Parse the JSON and construct the graph's model objects.
        raise NotImplementedError

    def save_map(self, graph: Graph) -> None:
        """Save the graph's locations and paths as JSON."""
        # TODO: Serialize the graph using the sample map's JSON structure.
        raise NotImplementedError
