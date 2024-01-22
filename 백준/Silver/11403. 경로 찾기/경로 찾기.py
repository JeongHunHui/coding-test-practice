# 23:35
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (grid[i][k] == 1 and grid[k][j] == 1) or grid[i][j] == 1:
                grid[i][j] = 1

for r in grid:
    print(' '.join(map(str, r)))