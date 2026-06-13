# Sudoku Solver

A simple Python CLI application that solves standard 9x9 Sudoku puzzles using a backtracking algorithm.

## Features

- Solves standard 9x9 Sudoku puzzles
- Validates puzzle size and duplicate conflicts
- Accepts `0` or `.` for empty cells
- Supports single-line or multi-line input
- Pure Python, no external dependencies

## Run

```bash
python sudoku_solver.py "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
```

You can also run it without arguments and paste a puzzle via standard input:

```bash
python sudoku_solver.py
```

## Input formats

### Single line

```text
530070000600195000098000060800060003400803001700020006060000280000419005000080079
```

### Multi-line grid

```text
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

## Output

```text
Solved Sudoku:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```
