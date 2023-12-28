# 17:58
import sys
sys.setrecursionlimit(100000)
t = int(input())
tc_list = []
for _ in range(t):
  m, n, k = map(int, input().split())
  tc_list.append((m, n, [list(map(int, input().split())) for _ in range(k)]))

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(x, y, m, n, grid):
  grid[y][x] = 0
  for dx, dy in dirs:
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[ny][nx] == 1:
      dfs(nx, ny, m, n, grid)

for m, n, data_list in tc_list:
  grid = [[0]*m for _ in range(n)]
  for tx, ty in data_list:
    grid[ty][tx] = 1
  count = 0
  for y in range(n):
    for x in range(m):
      if grid[y][x] == 1:
        count += 1
        dfs(x, y, m, n, grid)
  print(count)