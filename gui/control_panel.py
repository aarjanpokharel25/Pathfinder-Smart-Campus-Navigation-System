"""Tkinter controls for route search and map editing."""

import tkinter as tk
from typing import Tuple


class ControlPanel(tk.Frame):
    """Provide route-selection and campus-map editing controls."""

    def __init__(self, master: tk.Misc, **kwargs: object) -> None:
        """Create controls for choosing and editing campus routes."""
        super().__init__(master, **kwargs)
        # TODO: Add start/destination selectors, search buttons, and controls
        # for locations and paths.

    def get_route_selection(self) -> Tuple[str, str]:
        """Return the selected start and destination location IDs."""
        # TODO: Read and return the values from the selection controls.
        raise NotImplementedError
