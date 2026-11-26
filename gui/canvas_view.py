"""Canvas widget for drawing and animating campus routes."""

import tkinter as tk
from typing import List

from core.graph import Graph


class CanvasView(tk.Canvas):
    """Draw campus locations, paths, and route-search progress."""

    def __init__(self, master: tk.Misc, graph: Graph, **kwargs: object) -> None:
        """Create a canvas view for the supplied graph."""
        super().__init__(master, **kwargs)
        self.graph = graph

    def draw_map(self) -> None:
        """Draw all locations and paths on the canvas."""
        # TODO: Render the current graph.
        raise NotImplementedError

    def animate_search(self, explored_ids: List[str], path_ids: List[str]) -> None:
        """Animate explored locations and the final route."""
        # TODO: Schedule incremental canvas updates with Tkinter's after().
        raise NotImplementedError
