#!/usr/bin/env python3
"""Simple Sudoku solver CLI using backtracking."""

from __future__ import annotations

import sys
from typing import List, Optional, Tuple

Grid = List[List[int]]


class SudokuError(ValueError):
    """Raised when a Sudoku puzzle is invalid."""


def parse_puzzle(raw: str) -> Grid:
    """Parse a Sudoku puzzle from a string.

    Accepts:
    - 81-character single-line strings using digits and optional '.' for blanks
    - Multi-line grids containing digits, spaces, pipes, and dashes
    - 0 or . for empty cells
    """
    filtered = [ch for ch in raw if ch.isdigit() or ch == "."]
    if len(filtered) != 81:
        raise SudokuError(
            f"Expected 81 cells, but found {len(filtered)}. "
            "Use digits 1-9 and 0 or . for empty cells."
        )

    values = []
    for ch in filtered:
        if ch in {"0", "."}:
            values.append(0)
        else:
            values.append(int(ch))

    grid = [values[i:i + 9] for i in range(0, 81, 9)]
    validate_grid(grid)
    return grid


def validate_grid(grid: Grid) -> None:
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise SudokuError("Puzzle must be a 9x9 grid.")

    for row in grid:
        for value in row:
            if not isinstance(value, int) or value < 0 or value > 9:
                raise SudokuError("Puzzle values must be integers from 0 to 9.")

    for i in range(9):
        row_values = [v for v in grid[i] if v != 0]
        if len(row_values) != len(set(row_values)):
            raise SudokuError(f"Duplicate value found in row {i + 1}.")

        col_values = [grid[r][i] for r in range(9) if grid[r][i] != 0]
        if len(col_values) != len(set(col_values)):
            raise SudokuError(f"Duplicate value found in column {i + 1}.")

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box_values = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    value = grid[r][c]
                    if value != 0:
                        box_values.append(value)
            if len(box_values) != len(set(box_values)):
                raise SudokuError(
                    "Duplicate value found in 3x3 box starting at "
                    f"row {box_row + 1}, column {box_col + 1}."
                )


def find_empty(grid: Grid) -> Optional[Tuple[int, int]]:
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid_move(grid: Grid, row: int, col: int, num: int) -> bool:
    if any(grid[row][c] == num for c in range(9)):
        return False
    if any(grid[r][col] == num for r in range(9)):
        return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def solve(grid: Grid) -> bool:
    empty = find_empty(grid)
    if empty is None:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0

    return False


def format_grid(grid: Grid) -> str:
    lines = []
    for i, row in enumerate(grid):
        if i and i % 3 == 0:
            lines.append("------+-------+------")
        chunks = []
        for j in range(0, 9, 3):
            chunks.append(" ".join(str(n) for n in row[j:j + 3]))
        lines.append(" | ".join(chunks))
    return "\n".join(lines)


def read_puzzle_from_stdin() -> str:
    print("Paste a Sudoku puzzle (81 digits, or a 9x9 grid using 0 or . for blanks).")
    print("Press Ctrl-D (Unix/macOS) or Ctrl-Z then Enter (Windows) when done:\n")
    return sys.stdin.read()


def main(argv: List[str]) -> int:
    raw = argv[1] if len(argv) > 1 else read_puzzle_from_stdin()

    try:
        grid = parse_puzzle(raw)
    except SudokuError as exc:
        print(f"Invalid puzzle: {exc}", file=sys.stderr)
        return 1

    if not solve(grid):
        print("This puzzle has no solution.", file=sys.stderr)
        return 2

    print("Solved Sudoku:\n")
    print(format_grid(grid))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
