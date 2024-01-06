# 12:08
from collections import deque
m, n, k = map(int, input().split())
grid = [[True]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = False

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x, y):
    que = deque([(x, y)])
    grid[y][x] = False
    count = 0
    while que:
        x, y = que.popleft()
        count += 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[ny][nx]:
                grid[ny][nx] = False
                que.append((nx, ny))
    return count
counts = []
for y in range(m):
    for x in range(n):
        if grid[y][x]:
            count = bfs(x,y)
            if count > 0:
                counts.append(count)
print(len(counts))
print(' '.join(map(str, sorted(counts))))