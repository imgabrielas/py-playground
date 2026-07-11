# Sudoku Solver

A backtracking Sudoku solver that fills in a hardcoded 9x9 puzzle and renders the completed grid with `matplotlib`.

## How It Works

- The puzzle is defined as a 9x9 grid in `sudoku_grid`, where `0` marks an empty cell.
- `solve()` scans for the next empty cell and recursively tries numbers 1-9, backtracking whenever a choice leads to a dead end, until the grid is full.
- `is_valid()` checks a candidate number against its row, column, and 3x3 box before it's placed.
- Once solved, `draw_grid()` renders the finished grid as a matplotlib figure with bold 3x3 box borders and the solved numbers.

## Project Structure

| File | Description |
|---|---|
| `sudoku_solver.py` | Puzzle grid, backtracking solver, validity checks, and matplotlib rendering |

## Requirements

- Python 3.x
- `matplotlib`

```bash
pip install matplotlib
```

## Running

```bash
python sudoku_solver.py
```

A window titled "Sudoku Solver" opens showing the solved grid.

## Customizing the Puzzle

Edit the `sudoku_grid` list in `sudoku_solver.py` to solve a different puzzle. Use `0` for empty cells and `1`-`9` for givens.