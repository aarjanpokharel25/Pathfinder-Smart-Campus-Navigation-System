# CampusNav: Shortest Path Finder Using Dijkstra's and A* Algorithms

## Project structure

```text
.
├── algorithms/
│   ├── __init__.py
│   ├── astar.py
│   └── dijkstra.py
├── core/
│   ├── __init__.py
│   ├── graph.py
│   ├── location.py
│   └── path.py
├── data/
│   └── campus_map.json
├── gui/
│   ├── __init__.py
│   ├── app.py
│   ├── canvas_view.py
│   └── control_panel.py
├── tests/
│   ├── __init__.py
│   ├── test_astar.py
│   ├── test_dijkstra.py
│   └── test_graph.py
├── utils/
│   ├── __init__.py
│   └── map_manager.py
├── main.py
├── README.md
└── requirements.txt
```

CampusNav is a desktop campus navigation project for Python 3.8+ and
Tkinter. Its map is a weighted graph stored as an adjacency list. Users will
be able to select locations, compare Dijkstra's and A* search, animate
searches, edit the map, and block or unblock paths. Campus map data is stored
in JSON. The algorithm modules are separate from Tkinter so they can be used
and tested independently.

## File guide and team ownership

| File | Purpose | Team owner |
| --- | --- | --- |
| `main.py` | Starts the Tkinter application. | 3 — GUI |
| `core/__init__.py` | Marks the core models as a Python package. | 1 — Graph and map management |
| `core/location.py` | Defines a campus location and its coordinates. | 1 — Graph and map management |
| `core/path.py` | Defines a weighted, blockable connection. | 1 — Graph and map management |
| `core/graph.py` | Stores locations and weighted paths in an adjacency list. | 1 — Graph and map management |
| `algorithms/__init__.py` | Marks the search algorithms as a Python package. | 2 — Algorithms |
| `algorithms/dijkstra.py` | Dijkstra shortest-path search and metrics. | 2 — Algorithms |
| `algorithms/astar.py` | A* search and Euclidean heuristic. | 2 — Algorithms |
| `utils/map_manager.py` | Loads and saves graph data as JSON. | 1 — Graph and map management |
| `utils/__init__.py` | Marks the utilities as a Python package. | 1 — Graph and map management |
| `data/campus_map.json` | Sample campus map with eight locations. | 1 — Graph and map management |
| `gui/__init__.py` | Marks the Tkinter interface as a Python package. | 3 — GUI |
| `gui/app.py` | Connects the window, map view, and controls. | 3 — GUI |
| `gui/canvas_view.py` | Draws the graph and animates route search. | 3 — GUI |
| `gui/control_panel.py` | Provides route and map-editing controls. | 3 — GUI |
| `tests/__init__.py` | Marks the unit tests as a Python package. | 4 — Testing and documentation |
| `tests/test_graph.py` | Starter unit tests for graph behavior. | 4 — Testing and documentation |
| `tests/test_dijkstra.py` | Starter unit tests for Dijkstra search. | 4 — Testing and documentation |
| `tests/test_astar.py` | Starter unit tests for A* search. | 4 — Testing and documentation |
| `requirements.txt` | Documents that the project uses only the standard library. | 4 — Testing and documentation |
| `README.md` | Project overview, structure, ownership, and run commands. | 4 — Testing and documentation |

## Algorithm result

Both `find_path` methods are designed to return a tuple in this order:
`(path, total_distance, nodes_explored, execution_time)`. The path is a list of
location IDs and execution time is measured in seconds. Search implementations
are intentionally left as TODOs in this starter scaffold.

## Run the application and tests

From the project root:

```bash
python main.py
python -m unittest discover -s tests
```
