"""Output writer for A-Maze-ing."""


def write_output(
    file_path: str,
    hex_grid: list[str],
    entry_pos: tuple[int, int],
    exit_pos: tuple[int, int],
    path: str,
) -> None:
    """
    Write the maze output to a file.
    Args:
        file_path: Path to the output file.
        hex_grid: List of strings representing the maze layout in hex format.
        entry_pos: Tuple (x, y) for the entry point.
        exit_pos: Tuple (x, y) for the exit point.
        path: The solution path as a string.
    The output file format is:
    - Hex maze layout (one line per row)
    - Blank line
    - Entry point (x,y)
    - Exit point (x,y)
    - Solution path
    """
    if not file_path or not isinstance(file_path, str):
        print("Error: Invalid file path")
        return
    if not hex_grid or not isinstance(hex_grid, list):
        print("Error: Empty list")
        return
    if not isinstance(entry_pos, tuple) or len(entry_pos) != 2:
        print("Error: format entry_pos = (x, y)")
        return
    if not isinstance(path, str):
        print("Error: Path must be a string")
        return
    try:
        with open(file_path, "w") as f:
            # 1. The HL maze layout, one line per row
            for row in hex_grid:
                f.write(row + "\n")
            # 2. Put a blank line, then entry and exit positions router
            f.write("\n")
            f.write(f"{entry_pos[0]},{entry_pos[1]}\n")
            f.write(f"{exit_pos[0]},{exit_pos[1]}\n")
            # 3. Then the solution path
            f.write(path + "\n")
    except IOError as e:
        print(f"Error writing output file: {e}")
