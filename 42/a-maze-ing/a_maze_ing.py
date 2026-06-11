"""
A-MAZE-ING: A Maze Generator and Solver
Init point for the maze generator and solver. Reads configuration from a file,
generates the maze, writes the output, and displays it using curses.
"""

import sys

from core.config_parser import parse_config
from core.output_writer import write_output
from display.curses_display import run
from maze_generator.generator import maze_generator


def main() -> None:
    """Run the maze generator from a config file."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    cnf = parse_config(sys.argv[1])
    if cnf is None:
        sys.exit(1)

    seed = cnf.get("SEED")
    gen = maze_generator(
        width=cnf["WIDTH"],
        height=cnf["HEIGHT"],
        seed=seed,
        perfect=cnf["PERFECT"],
    )
    gen.generate(start_pos=cnf["ENTRY"])

    write_output(
        cnf["OUTPUT_FILE"],
        gen.get_hex_layout(),
        cnf["ENTRY"],
        cnf["EXIT"],
        gen.solve(start=cnf["ENTRY"], end=cnf["EXIT"]),
    )

    run(
        width=cnf["WIDTH"],
        height=cnf["HEIGHT"],
        entry=cnf["ENTRY"],
        exit_=cnf["EXIT"],
        seed=seed,
        perfect=cnf["PERFECT"],
    )


# Run
if __name__ == "__main__":
    main()
