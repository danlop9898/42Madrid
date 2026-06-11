*This project has been created as part of the 42 curriculum by igramos- and dalopez3*

# A-Maze-ing

## Description

A-Maze-ing is a maze generator written in Python. It takes a configuration file,
generates a perfect maze using a recursive backtracking algorithm, writes it to a
file in hexadecimal format, and displays it visually in the terminal using curses.
The maze includes a hidden "42" pattern, a BFS-based solver, and an interactive
display with color themes and animated path visualization.



## Instructions

### Installation

``` 
make install
```

### Run

``` 
make run
```

Or directly:

``` 
python3 a_maze_ing.py config.txt
```

### Lint

``` 
make lint
```

### Debug

``` 
make debug
```

### Clean

``` 
make clean
```

### Build the pip package

``` 
make build
```

## Configuration File

The configuration file must contain one `KEY=VALUE` pair per line.
Lines starting with `# ` are treated as comments and ignored.

| **Key** | **Description** | **Example** |
| ------- | --------------- | ----------- |
| `WIDTH` | *Maze width in cells* | `WIDTH=20` |
| `HEIGHT` | *Maze height in cells* | `HEIGHT=15`|
| `ENTRY` | *Start entry coordinates (x, y)* | `ENTRY=0,0` |
| `EXIT` | *Finish exit coordinates (x, y)* | `EXIT=19,14` |
| `OUTPUT_FILE` | *Output filename* | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | *Generate a perfect maze* | `PERFECT=True` |
| `SEED` | *Optional seed for reproducibility* | `SEED=42` |

Example `config.txt`:
```
WIDTH=20
HEIGHT=15
SEED=42
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
```

## Maze Generation Algorithm

The maze is generated using the **randomized recursive backtracking**(RRBT) algorithm (also known as recursive DFS). Starting from a given cell, the algorithm recursively visits unvisited neighbours in a random order, carving passages between them, and backtracks when no unvisited neighbours remain.

### Why this algorithm?

Recursive backtracking (RRBT) was selected for its optimal computational properties and pedagogical value. The algorithm guarantees perfect maze generation with *O(n)* complexity, ensuring deterministic spanning tree properties. The depth-first traversal approach maps efficiently onto bitmask representations, minimizing memory overhead while maintaining wall cardinality constraints. This technique also preserves orthogonal cell adjacency, critical for BFS pathfinding integration and the *"42"* pattern embedding without topological violations.

## Display

The terminal display is built with Python's `curses` library. User interactions:

- **Arrow keys + Enter** — Navigate the menu
- **Re-generate** — Generate a new maze
- **Show/Hide path** — Animate and display the shortest solution path
- **Rotate colors** — Cycle through color themes 
- **Quit** — Exit the program

## Reusable Module

The maze generation logic is packaged as a standalone pip-installable module located at the root of this repository.

### Installation

``` 
pip install amazeing-0.1.0-py3-none-any.whl
```

### Usage

``` python
from maze_generator.generator import maze_generator

# Instantiate with custom size and seed
gen = maze_generator(width=20, height=15, seed=42)

# Generate the maze starting from (0, 0)
gen.generate(start_pos=(0, 0))

# Access the grid (2D list of bitmasks)
print(gen.grid)

# Get hex layout (list of strings, one per row)
for row in gen.get_hex_layout():
    print(row)

# Solve: returns path as N/E/S/W string
solution = gen.solve(start=(0, 0), end=(19, 14))
print(solution)
```

### Parameters

| **Parameter** | **Type** | **Description** |
| ------------- | -------- | --------------- |
| `width` | `int` | Maze width in cells |
| `height` | `int` | Maze height in cells |
| `seed` | `int` | Optional seed for reproducibility |

### Methods

| **Method** | **Returns** | **Description** |
| ---------- | ----------- | --------------- |
| `generate(start_pos)` | `None` | Generate the maze |
| `solve(start, end)` | `str` | BFS shortest path as N/E/S/W string |
| `get_hex_layout()` | `list[str]` | Maze as hex strings |
| `validate_no_2x2_area()` | `bool` | Check no illegal open areas exist |
 
  
### Tools used

- **VS Code** — Primary editor for both team members
- **Git / GitHub** — Version control with feature branches and pull requests
- **pip / venv** — Dependency management and isolated development environment
- **flake8** — Code style and linting
- **mypy** — Static type checking
- **pytest** — Unit testing
- **Python build** — Packaging the reusable maze_generator module

 

## Resources
- [Artificial Intelligence Search Problem: Solve Maze using Breadth First Search (BFS) Algorithm] 
- [1STS](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/) 
- [Creating Menu Display for Terminal](https://www.youtube.com/watch?v=zwMsmBsC1GM)


### VENV / Wheel install WHL

Create VENV
- python3 -m venv venv_test
- source venv_test/bin/activate

Input WHL into VENV
- *navigate into folder*
- pip install <pkg whl>
- python3

Check pkg
- pip show <pkg>

### Roles
dalopez3: Logic (config parser, perfect/imperfect maze), Testing, QA, Documentation
igramos-: Logic (trace, drawing), Theming, UI, Documentation


### AI Usage

AI was used during this project for the following tasks:

- Generating an initial project plan and structure, including file responsibilities per team member
- Suggesting git workflows and commands for branch-based collaboration
- Reviewing code against project requirements (flake8, mypy, docstrings, type hints)
- Pair coded aid.
- Debug type errors and fixing formatting inconsistencies.
- Generate aid text for doc.

**All code logic and implementation were written and understood by the team.**