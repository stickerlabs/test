# Sudoku Solver

A simple Python application that solves standard 9x9 Sudoku puzzles using a backtracking algorithm.

## Features

- Solves standard 9x9 Sudoku puzzles
- Validates input for correct format and constraints
- Displays solved puzzle in a readable grid format
- Fast backtracking algorithm
- Minimal dependencies (pure Python)

## Installation

```bash
git clone https://github.com/stickerlabs/test.git
cd test
```

## Usage

Run the solver with a Sudoku puzzle:

```bash
python sudoku_solver.py
```

You can input puzzles using:
- `0` or `.` to represent empty cells
- `1-9` for filled cells
- Each row separated by a new line or space

### Example Input Format

```
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

Or simply as a single line of 81 digits:
```
530070000600195000098000060800060003400803001700020006060000280000419005000080079
```

## Output

The solver will display the completed puzzle:

```
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

## How It Works

The solver uses a **backtracking algorithm**:
1. Find an empty cell
2. Try each number 1-9
3. Check if the number is valid (no conflicts in row, column, or 3x3 box)
4. If valid, place the number and recurse
5. If no valid number works, backtrack and try a different value

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT
