def tromino_tiling(board, size, top, left, missing_row, missing_col):
    # Base case: if the board is 2x2
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

    # Decide which quadrant the missing square is in
    if missing_row < center_row and missing_col < center_col:  
        # Missing square is in top-left
        quadrant = 0
    elif missing_row < center_row and missing_col >= center_col:  
        # Top-right
        quadrant = 1
    elif missing_row >= center_row and missing_col < center_col:  
        # Bottom-left
        quadrant = 2
    else:  
        # Bottom-right
        quadrant = 3

    # Place one tromino in the center covering three quadrants
    tile = 1
    if quadrant != 0: board[center_row-1][center_col-1] = tile
    if quadrant != 1: board[center_row-1][center_col] = tile
    if quadrant != 2: board[center_row][center_col-1] = tile
    if quadrant != 3: board[center_row][center_col] = tile

    # Recurse for each quadrant
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

# Example usage:
n = 4  # 4x4 board
board = [[0]*n for _ in range(n)]
board[0][1] = -1  # Mark missing square (row=0, col=1)

tromino_tiling(board, n, 0, 0, 0, 1)

# Print the board
for row in board:
    print(row)
