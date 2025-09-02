tromino_counter = 0

def get_new_tromino_id():
    global tromino_counter
    tromino_counter += 1
    return tromino_counter


def tromino_tiling(board, size, row, col, missing_row, missing_col):
    if size == 2:
        tromino_id = get_new_tromino_id()
        for r in range(row, row+2):
            for c in range(col, col+2):
                if (r, c) != (missing_row, missing_col):
                    board[r][c] = tromino_id
        return
    
    half = size // 2
    center_row, center_col = row + half, col + half

    
    if missing_row < center_row and missing_col < center_col:
        missing_quad = "TL"
    elif missing_row < center_row and missing_col >= center_col:
        missing_quad = "TR"
    elif missing_row >= center_row and missing_col < center_col:
        missing_quad = "BL"
    else:
        missing_quad = "BR"
    
    tromino_id = get_new_tromino_id()
    if missing_quad != "TL":
        board[center_row-1][center_col-1] = tromino_id
    if missing_quad != "TR":
        board[center_row-1][center_col] = tromino_id
    if missing_quad != "BL":
        board[center_row][center_col-1] = tromino_id
    if missing_quad != "BR":
        board[center_row][center_col] = tromino_id

    tromino_tiling(board, half, row, col, 
                   missing_row if missing_quad == "TL" else center_row-1,
                   missing_col if missing_quad == "TL" else center_col-1)

    tromino_tiling(board, half, row, center_col, 
                   missing_row if missing_quad == "TR" else center_row-1,
                   missing_col if missing_quad == "TR" else center_col)

    tromino_tiling(board, half, center_row, col, 
                   missing_row if missing_quad == "BL" else center_row,
                   missing_col if missing_quad == "BL" else center_col-1)

    tromino_tiling(board, half, center_row, center_col, 
                   missing_row if missing_quad == "BR" else center_row,
                   missing_col if missing_quad == "BR" else center_col)
    return board
size = 8 
board = [[0]*size for _ in range(size)]
missing_row, missing_col = 3, 3   
tromino_tiling(board, size, 0, 0, missing_row, missing_col)
for row in board:
    print(row)
print("Number of trominoes used:", tromino_counter)
