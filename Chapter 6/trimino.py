def tromino(board, size, x, y):
    # size = current square size
    # (x, y) = missing square inside this part

    # Base case: small 2x2 square
    if size == 2:
        num = 1  # use 1 to mark tiles
        for i in range(2):
            for j in range(2):
                if not (i == x and j == y):
                    board[i][j] = num
        return

    # Cut board into 4 smaller squares
    half = size // 2

    # Place 1 tromino in the middle (covers 3 squares)
    # (for simplicity, we just mark it with number 1)
    board[half-1][half] = 1
    board[half][half-1] = 1
    board[half][half] = 1

    # Call again on each smaller square
    tromino(board, half, x, y)              # top-left
    tromino(board, half, x, y)              # top-right
    tromino(board, half, x, y)              # bottom-left
    tromino(board, half, x, y)              # bottom-right

# Example: make 4x4 board
n = 4
board = [[0]*n for _ in range(n)]

# Missing square (say top-left corner)
board[0][0] = -1  

# Run the algorithm
tromino(board, n, 0, 0)

# Show result
for row in board:
    print(row)
