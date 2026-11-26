"""Location model for a point on the campus map."""


class Location:
    """A named campus location with two-dimensional map coordinates."""

    def __init__(self, location_id: str, name: str, x: float, y: float) -> None:
        """Create a location.

        Args:
            location_id: Unique identifier used by the graph and map file.
            name: Human-readable location name.
            x: Horizontal map coordinate.
            y: Vertical map coordinate.
        """
        self.location_id = location_id
        self.name = name
        self.x = x
        self.y = y
