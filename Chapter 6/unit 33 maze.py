def is_promising(x, y, maze, visited):
    n = len(maze)
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and not visited[x][y]

def solve_maze(maze):
    n = len(maze)
    visited = [[False]*n for _ in range(n)]
    path = [[1]*n for _ in range(n)]  
    

    def depth_first_search(x, y):
        if x == n-1 and y == n-1:  
            path[x][y] = 0
            return True
        
        if is_promising(x, y, maze, visited):
            visited[x][y] = True
            path[x][y] = 0

            
            if depth_first_search(x, y+1): return True
            if depth_first_search(x+1, y): return True
            if depth_first_search(x, y-1): return True
            if depth_first_search(x-1, y): return True

            
            path[x][y] = 1
            return False
        return False

    depth_first_search(0, 0)
    return path


maze = [[0,0,0,0],
        [1,0,1,0],
        [1,0,1,1],
        [0,0,0,0]]

solution = solve_maze(maze)
print("Solution Path (0 = path, 1 = wall):")
for row in solution:
    print(*row)
