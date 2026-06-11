"""
Maze generator with bit logic, 42 pattern, and BFS solver.
BFS solver is used to find the shortest path from entry to exit.
The maze is represented as a grid of integers, where each bit represents wall:
- Bit 0 (1): North wall
- Bit 1 (2): East wall
- Bit 2 (4): South wall
- Bit 3 (8): West wall

Cell: WSEN = 15 (all walls)

The generator uses a recursive backtracking algorithm to carve passages.
"""

import random
import sys
from collections import deque
from typing import Iterator, Optional

N, E, S, W = 1, 2, 4, 8
OPPOSITE = {N: S, S: N, E: W, W: E}
MOVE = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}
DIR_MAP = {N: "N", E: "E", S: "S", W: "W"}

MIN_SIZE_FOR_42 = 10

sys.setrecursionlimit(1_000_000)


class maze_generator:
    """
    Modular generator for mazes with bit logic, 42 pattern, and BFS solver."""

    def __init__(
        self,
        width: int,
        height: int,
        seed: Optional[int] = None,
        perfect: bool = True,
    ) -> None:
        """
        Init the generator.
        Args:
            width: is the width of the maze in cells.
            height: is the height of the maze in cells.
            seed: Optional seed for reproducible results.
            perfect: If True, generate a perfect maze (is SINGLE way).
        """
        self.width = width
        self.height = height
        self.seed = seed
        self.perfect = perfect
        self.grid: list[list[int]] = []
        self.visited: set[tuple[int, int]] = set()

    def _apply_42_pattern(self) -> None:
        """
        Reserves cells for the '42' pattern before generation.
        Prints a warning if the maze is too small."""
        if self.width < MIN_SIZE_FOR_42 or self.height < MIN_SIZE_FOR_42:
            print("Warning: Maze too small to display '42' pattern.")
            return

        offset_x = max(0, self.width // 2 - 3)
        offset_y = max(0, self.height // 2 - 2)

        # Coordinates for the "4" and "2" digits (middle)
        pattern = [
            (0, 0), (0, 1), (0, 2), (1, 2), (2, 0),
            (2, 1), (2, 2), (2, 3), (2, 4), (4, 0),
            (5, 0), (6, 0), (6, 1), (6, 2), (5, 2),
            (4, 2), (4, 3), (4, 4), (5, 4), (6, 4),
        ]
        for px, py in pattern:
            nx, ny = offset_x + px, offset_y + py
            if 0 <= nx < self.width and 0 <= ny < self.height:
                self.visited.add((nx, ny))

    def _find_valid_start(
        self, start_pos: tuple[int, int],
    ) -> tuple[int, int]:
        """Find a valid starting cell that is within bounds and not reserved.

        Args:
            start_pos: Preferred starting position.

        Returns:
            A valid (x, y) starting cell.
        """
        sx, sy = start_pos
        if (
            0 <= sx < self.width
            and 0 <= sy < self.height
            and (sx, sy) not in self.visited
        ):
            return start_pos
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) not in self.visited:
                    return (x, y)
        return (0, 0)

    def generate(self, start_pos: tuple[int, int] = (0, 0)) -> None:
        """Generates the maze using the backtracking algorithm.

        Args:
            start_pos: Start coordinates for the algorithm.
        """
        if self.seed is not None:
            random.seed(self.seed)

        self.grid = [
            [15 for _ in range(self.width)]
            for _ in range(self.height)
        ]
        self.visited = set()

        self._apply_42_pattern()

        actual_start = self._find_valid_start(start_pos)
        self._backtrack(actual_start[0], actual_start[1])

        if not self.perfect:
            self._remove_extra_walls()

    def generate_animated(
        self, start_pos: tuple[int, int] = (0, 0),
    ) -> Iterator[tuple[int, int]]:
        """Generate the maze and yield each carved cell for animation.

        Args:
            start_pos: initial position for the algorithm.

        Yields:
            (x, y) tuple for each newly cell is carved.
        """
        if self.seed is not None:
            random.seed(self.seed)

        self.grid = [
            [15 for _ in range(self.width)]
            for _ in range(self.height)
        ]
        self.visited = set()

        self._apply_42_pattern()

        actual_start = self._find_valid_start(start_pos)
        yield from self._backtrack_animated(actual_start[0], actual_start[1])

        if not self.perfect:
            self._remove_extra_walls()

    def _backtrack(self, x: int, y: int) -> None:
        """Recursive backtracking algorithm for generating passages.

        Args:
            x: Current X-coordinate.
            y: Current Y-coordinate.
        """
        self.visited.add((x, y))
        directions = list(MOVE.keys())
        random.shuffle(directions)

        for direction in directions:
            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and (nx, ny) not in self.visited
            ):
                self.grid[y][x] &= ~direction
                self.grid[ny][nx] &= ~OPPOSITE[direction]
                self._backtrack(nx, ny)

    def _backtrack_animated(
        self, x: int, y: int,
    ) -> Iterator[tuple[int, int]]:
        """Backtracking that yields each carved cell for animation.

        Args:
            x: current X-coordinate.
            y: current Y-coordinate.

        Yields:
            (x, y) tuple for each newly carved cell.
        """
        self.visited.add((x, y))
        yield (x, y)
        directions = list(MOVE.keys())
        random.shuffle(directions)

        for direction in directions:
            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and (nx, ny) not in self.visited
            ):
                self.grid[y][x] &= ~direction
                self.grid[ny][nx] &= ~OPPOSITE[direction]
                yield from self._backtrack_animated(nx, ny)

    def _remove_extra_walls(self) -> None:
        """Remove some random walls to create loops (non-perfect maze)."""
        candidates: list[tuple[int, int, int]] = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 15:
                    continue
                for direction in (E, S):
                    if not (self.grid[y][x] & direction):
                        continue
                    dx, dy = MOVE[direction]
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < self.width
                        and 0 <= ny < self.height
                        and self.grid[ny][nx] != 15
                    ):
                        candidates.append((x, y, direction))
        random.shuffle(candidates)
        to_remove = max(1, len(candidates) // 8)
        for x, y, direction in candidates[:to_remove]:
            dx, dy = MOVE[direction]
            nx, ny = x + dx, y + dy
            self.grid[y][x] &= ~direction
            self.grid[ny][nx] &= ~OPPOSITE[direction]

    def solve(self, start: tuple[int, int], end: tuple[int, int]) -> str:
        """Finds the shortest path from start to end using BFS.

        Args:
            start: Start point as (x, y).
            end: End point as (x, y).

        Returns:
            Path as a string of N/E/S/W, or an empty string if no path exists.
        """
        queue: deque[tuple[tuple[int, int], str]] = deque([(start, "")])
        visited_solve: set[tuple[int, int]] = {start}

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path
            for direction, (dx, dy) in MOVE.items():
                nx, ny = x + dx, y + dy
                # Check if path is open (bit not set)
                # and within the boundaries
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (
                        not (self.grid[y][x] & direction)
                        and (nx, ny) not in visited_solve
                    ):
                        visited_solve.add((nx, ny))
                        queue.append(((nx, ny), path + DIR_MAP[direction]))
        return ""

    def validate_no_3x3_area(self) -> bool:
        """Check that no 3x3 fully open area exists in the maze.

        The subject allows up to 2x3 / 3x2 open areas but forbids 3x3.

        Returns:
            True if no violation found, False otherwise.
        """
        for y in range(self.height - 2):
            for x in range(self.width - 2):
                open_area = True
                for dy in range(3):
                    for dx in range(3):
                        cx, cy = x + dx, y + dy
                        if dx < 2 and (self.grid[cy][cx] & E):
                            open_area = False
                        if dy < 2 and (self.grid[cy][cx] & S):
                            open_area = False
                        if not open_area:
                            break
                    if not open_area:
                        break
                if open_area:
                    return False
        return True

    def get_hex_layout(self) -> list[str]:

        """
        Returns the maze as a list of hexadecimal strings.

        Returns:
        List of strings, one per line, each cell as a hexadecimal digit.

        """
        return ["".join(f"{cell:X}" for cell in row) for row in self.grid]
