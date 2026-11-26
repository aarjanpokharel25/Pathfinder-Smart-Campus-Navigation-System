"""Main Tkinter application window."""

import tkinter as tk

from gui.canvas_view import CanvasView
from gui.control_panel import ControlPanel


class App:
    """Coordinate the CampusNav window, map view, and controls."""

    def __init__(self) -> None:
        """Create the root window and its main interface components."""
        self.root = tk.Tk()
        self.root.title("CampusNav")
        # TODO: Load the campus map and connect the view and control callbacks.

    def run(self) -> None:
        """Start the Tkinter event loop."""
        self.root.mainloop()
