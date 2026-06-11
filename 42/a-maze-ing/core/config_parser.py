"""Configuration file parser for A-Maze-ing."""

from typing import Any
import sys

REQUIRED_KEYS = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}


def parse_config(filename: str) -> dict[str, Any] | None:
    """Read and validate the configuration file.

    Args:
        filename: Path to the configuration file.

    Returns:
        Dictionary with configuration values, or None on error.
    """
    config: dict[str, Any] = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    print("Error: Invalid line")
                    return None
                key, value = line.split("=", 1)
                key = key.strip().upper()
                value = value.strip()
                if key in ("WIDTH", "HEIGHT", "SEED"):
                    config[key] = int(value)
                elif key in ("ENTRY", "EXIT"):
                    config[key] = tuple(map(int, value.split(",")))
                elif key == "PERFECT":
                    val = value.strip().lower()
                    if val not in ("true", "false"):
                        print("Error in PERFECT value, true or false")
                        return None
                    config[key] = (val == "true")

                else:
                    config[key] = value

    except FileNotFoundError:
        print(f"Error: Config file '{filename}' not found.")
        return None
    except ValueError as e:
        print(f"Error: Invalid value in configuration file: {e}")
        return None

    missing = REQUIRED_KEYS - config.keys()
    if missing:
        print(f"Error: Missing required keys: {', '.join(sorted(missing))}")
        return None

    width = config.get("WIDTH")
    height = config.get("HEIGHT")
    if not isinstance(width, int) or not isinstance(height, int):
        print("Error: WIDTH and HEIGHT must be integers.")
        return None
    if width < 1 or height < 1:
        print(
            f"Error: Dimensions must be positive "
            f"(got {width}x{height})."
        )
        return None

    entry = config["ENTRY"]
    exit_ = config["EXIT"]

    def es_xy(val):
        return (
            isinstance(val, tuple) and
            len(val) == 2 and
            all(isinstance(v, (int, float)) for v in val)
        )

    if not es_xy(entry) or not es_xy(exit_):
        print("Error: Invalid value in ENTRY/EXIT. Must be x,y")
        sys.exit(1)

    ex, ey = entry
    sx, sy = exit_
    bounds = f"{width}x{height}"
    if not (0 <= ex < width and 0 <= ey < height):
        print(f"Error: ENTRY {entry} out of bounds ({bounds}).")
        return None
    if not (0 <= sx < width and 0 <= sy < height):
        print(f"Error: EXIT {exit_} out of bounds ({bounds}).")
        return None
    if entry == exit_:
        print("Error: ENTRY and EXIT must be not same point.")
        return None

    # function To avoid collisions for 42 pattern
    def get_42_cells(width, height):
        if width < 7 or height < 5:
            return set()
        offset_x = max(0, width // 2 - 3)
        offset_y = max(0, height // 2 - 2)

        pattern = [
            (0, 0), (0, 1), (0, 2), (1, 2), (2, 0),
            (2, 1), (2, 2), (2, 3), (2, 4), (4, 0),
            (5, 0), (6, 0), (6, 1), (6, 2), (5, 2),
            (4, 2), (4, 3), (4, 4), (5, 4), (6, 4),
        ]

        cells = set()
        for px, py in pattern:
            nx, ny = offset_x + px, offset_y + py
            if 0 <= nx < width and 0 <= ny < height:
                cells.add((nx, ny))

        return cells

    # Check collisions 42 pattern
    if entry in get_42_cells(width, height):
        print("Error: ENTRY overlaps with '42' pattern.")
        return None
    if exit_ in get_42_cells(width, height):
        print("Error: EXIT overlaps with '42' pattern.")
        return None

    return config
