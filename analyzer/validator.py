# validator.py file
import math

def get_box_start_coordinate(x, y):
    return 3 * int(math.floor(x/3)), 3 * int(math.floor(y/3))

def validate_sudoku(board):
    for x, i in enumerate(board):
        for y, j in enumerate(i):
            if j != 0:
                for p in range(9):
                    if p != x and j == board[p][y]:
                        return (False, f'Horizontal wrong input in cell ({x},{y})!')
                    if p != y and j == board[x][p]:
                        return (False, f'Vertical wrong input in cell ({x},{y})!')
                i_n, j_n = get_box_start_coordinate(x, y)
                for (i, j) in [(i, j) for p in range(i_n, i_n + 3) for q in range(j_n, j_n + 3)
                               if (p, q) != (x, y) and j == board[p][q]]:
                                    return (False, f'Box wrong input in cell ({x},{y})!')
    return (True, 'Solvable')