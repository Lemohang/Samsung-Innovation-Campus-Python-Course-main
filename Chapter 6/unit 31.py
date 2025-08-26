tromino_counter = 0

def get_new_tromino_id():
    global tromino_counter
    tromino_counter += 1
    return tromino_counter


def tromino_tiling(board, size, row, col, defect_row, defect_col):
    if size == 2:
        tromino_id = get_new_tromino_id()
        for r in range(row, row+2):
            for c in range(col, col+2):
                if (r, c) != (defect_row, defect_col):
                    board[r][c] = tromino_id
        return
    
    half = size // 2
    center_row, center_col = row + half, col + half

    # Find which quadrant has the defect
    if defect_row < center_row and defect_col < center_col:
        defect_quad = "TL"
    elif defect_row < center_row and defect_col >= center_col:
        defect_quad = "TR"
    elif defect_row >= center_row and defect_col < center_col:
        defect_quad = "BL"
    else:
        defect_quad = "BR"
    
    tromino_id = get_new_tromino_id()
    if defect_quad != "TL":
        board[center_row-1][center_col-1] = tromino_id
    if defect_quad != "TR":
        board[center_row-1][center_col] = tromino_id
    if defect_quad != "BL":
        board[center_row][center_col-1] = tromino_id
    if defect_quad != "BR":
        board[center_row][center_col] = tromino_id

    tromino_tiling(board, half, row, col, 
                   defect_row if defect_quad == "TL" else center_row-1,
                   defect_col if defect_quad == "TL" else center_col-1)

    tromino_tiling(board, half, row, center_col, 
                   defect_row if defect_quad == "TR" else center_row-1,
                   defect_col if defect_quad == "TR" else center_col)

    tromino_tiling(board, half, center_row, col, 
                   defect_row if defect_quad == "BL" else center_row,
                   defect_col if defect_quad == "BL" else center_col-1)

    tromino_tiling(board, half, center_row, center_col, 
                   defect_row if defect_quad == "BR" else center_row,
                   defect_col if defect_quad == "BR" else center_col)
    return board
size = 8 
board = [[0]*size for _ in range(size)]
defect_row, defect_col = 3, 3   
tromino_tiling(board, size, 0, 0, defect_row, defect_col)
for row in board:
    print(row)
print("Number of trominoes used:", tromino_counter)
