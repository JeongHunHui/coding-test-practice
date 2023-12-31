# 22:24
import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split())
grid = [[0] * (m+1) for _ in range(n+1)]
for _ in range(k):
    y, x = map(int, input().split())
    grid[y][x] = 1
answer = 0

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(grid, x, y, count):
    grid[y][x] = 0
    count += 1
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < m+1 and ny >= 0 and ny < n+1 and grid[ny][nx] == 1:
            count += dfs(grid, nx, ny, 0)
    return count

for y in range(1, n+1):
    for x in range(1, m+1):
        if grid[y][x] == 1:
            answer = max(dfs(grid, x, y, 0), answer)

print(answer)