"""Entry point for the CampusNav desktop application."""

from gui.app import App


def main() -> None:
    """Create and run the CampusNav application."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()
