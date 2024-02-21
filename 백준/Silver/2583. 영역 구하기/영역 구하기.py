# 02:45
import sys
sys.setrecursionlimit(100000)
m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
is_visited = [[False] * n for _ in range(m)]
def dfs(x, y, is_visited, total):
    is_visited[y][x] = True
    total += 1
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and not is_visited[ny][nx] and grid[ny][nx] == 0:
            total += dfs(nx,ny,is_visited,0)
    return total
answers = []
for y in range(m):
    for x in range(n):
        if not is_visited[y][x] and grid[y][x] == 0:
            answers.append(dfs(x,y,is_visited,0))
answers.sort()
print(len(answers))
print(' '.join(map(str, answers)))