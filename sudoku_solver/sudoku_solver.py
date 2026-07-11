import matplotlib.pyplot as plt

sudoku_grid = [
            [0,0,0,0,1,3,0,4,0],
            [0,1,0,0,9,0,0,0,5],
            [5,0,4,0,0,2,6,3,0],
            [4,0,1,0,0,6,3,0,0],
            [0,0,6,0,0,8,0,9,2],
            [9,0,2,3,0,0,5,1,0],
            [0,7,5,0,0,0,8,0,0],
            [3,0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0,9]
        ]

def is_valid(row_index, column_index, number):
    global sudoku_grid
    for n in range(0,9):
        if sudoku_grid[row_index][n] == number:
            return False
        
    for n in range(0,9):
        if sudoku_grid[n][column_index] == number:
            return False
        
    square_col = (column_index // 3) * 3
    square_row = (row_index // 3) * 3
    for n in range(0,3):
        for m in range(0,3):
            if sudoku_grid[square_row+n][square_col+m] == number:
                return False
    
    return True

def solve():
    global sudoku_grid
    for row in range(0,9):
        for column in range(0,9):
            if sudoku_grid[row][column] == 0:
                for number in (range(1,10)):
                    if is_valid(row, column, number):
                        sudoku_grid[row][column] = number
                        solve()
                        sudoku_grid[row][column] = 0
                return
            
    draw_grid()
    return

def draw_grid():
    global sudoku_grid
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        ax.plot([0, 9], [i, i], color='black', linewidth=line_width)
        ax.plot([i, i], [0, 9], color='black', linewidth=line_width)

    for row in range(9):
        for column in range(9):
            number = sudoku_grid[row][column]
            if number != 0:
                ax.text(column + 0.5, 9 - row - 0.5, str(number),
                        ha='center', va='center', fontsize=20)

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Here is your solution ;))', fontsize=16)

    fig.canvas.manager.set_window_title('Sudoku Solver')
    plt.tight_layout()
    plt.show()

solve()