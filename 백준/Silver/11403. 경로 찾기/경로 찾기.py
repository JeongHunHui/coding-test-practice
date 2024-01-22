# 23:35
import math
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (grid[i][k] > 0 and grid[k][j] > 0) or grid[i][j] > 0:
                grid[i][j] = 1

for r in grid:
    print(' '.join(list(map(str, r))))