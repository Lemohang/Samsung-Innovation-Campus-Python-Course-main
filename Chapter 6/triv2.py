def tromino_tiling(board, size, top, left, missing_row, missing_col):
    
    if size == 2:
        tile = 1
        for i in range(2):
            for j in range(2):
                if not (top + i == missing_row and left + j == missing_col):
                    board[top + i][left + j] = tile
        return
    
    half = size // 2
    center_row = top + half
    center_col = left + half


    if missing_row < center_row and missing_col < center_col:  

        quadrant = 0
    elif missing_row < center_row and missing_col >= center_col:  

        quadrant = 1
    elif missing_row >= center_row and missing_col < center_col: 

        quadrant = 2
    else:  

        quadrant = 3


    tile = 1
    if quadrant != 0: board[center_row-1][center_col-1] = tile
    if quadrant != 1: board[center_row-1][center_col] = tile
    if quadrant != 2: board[center_row][center_col-1] = tile
    if quadrant != 3: board[center_row][center_col] = tile

    
    tromino_tiling(board, half, top, left,
                   missing_row if quadrant == 0 else center_row-1,
                   missing_col if quadrant == 0 else center_col-1)

    tromino_tiling(board, half, top, center_col,
                   missing_row if quadrant == 1 else center_row-1,
                   missing_col if quadrant == 1 else center_col)

    tromino_tiling(board, half, center_row, left,
                   missing_row if quadrant == 2 else center_row,
                   missing_col if quadrant == 2 else center_col-1)

    tromino_tiling(board, half, center_row, center_col,
                   missing_row if quadrant == 3 else center_row,
                   missing_col if quadrant == 3 else center_col)


n = int(input("Enter the size of the board: "))
board = [[0]*n for _ in range(n)]
board[0][1] = -1 

tromino_tiling(board, n, 0, 0, 0, 1)


for row in board:
    print(row)
