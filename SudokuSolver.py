def find_cell_tofill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y

    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def is_valid(grid, i, j, e):
    row_ok = all([grid[i][y] != e for y in range(0, 9)]) 
    if row_ok:
        column_ok = all([grid[x][j] != e for x in range(0, 9)])
        if column_ok:
            sec_top_x, sec_top_y = 3*(i//3), 3*(j//3)
            for x in range(sec_top_x, sec_top_x+3):
                for y in range(sec_top_y, sec_top_y+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

def solve_sudoku(grid, i=0, j=0):
    i, j = find_cell_tofill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            if solve_sudoku(grid, i, j):
                return True
            grid[i][j] = 0   # the attempt e doesn't work, backtracking
    return False



sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(solve_sudoku(sudoku))

for row in sudoku:
    print(row)
