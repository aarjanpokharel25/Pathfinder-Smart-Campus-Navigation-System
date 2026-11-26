"""Path model for a weighted connection between two locations."""


class Path:
    """A weighted, optionally blocked, connection between two locations."""

    def __init__(
        self,
        start_id: str,
        end_id: str,
        distance: float,
        blocked: bool = False,
    ) -> None:
        """Create a path between two location identifiers.

        Args:
            start_id: Identifier of one endpoint.
            end_id: Identifier of the other endpoint.
            distance: Non-negative travel distance used as the edge weight.
            blocked: Whether this path is currently unavailable.
        """
        self.start_id = start_id
        self.end_id = end_id
        self.distance = distance
        self.blocked = blocked
