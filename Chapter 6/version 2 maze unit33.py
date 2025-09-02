def promising(x, y, maze, visited):
    n = len(maze)
    return (0 <= x < n and 0 <= y < n and
            maze[x][y] == 0 and not visited[x][y])

def solve_maze(x, y, maze, visited, path):
    n = len(maze)

    
    if x == n - 1 and y == n - 1:
        print("Path:", path)
        return True

    if promising(x, y, maze, visited):
        visited[x][y] = True 

        
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in moves:
            if solve_maze(x + dx, y + dy, maze, visited, path + [(x+dx, y+dy)]):
                return True

        visited[x][y] = False 
    return False


maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

n = len(maze)
visited = [[False] * n for _ in range(n)]
solve_maze(0, 0, maze, visited, [(0, 0)])
