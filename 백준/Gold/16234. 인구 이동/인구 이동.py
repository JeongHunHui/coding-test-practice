# 10:37
from collections import deque
n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[False] * n for _ in range(n)]
def bfs(x, y):
    visited[y][x] = True
    que = deque([(x,y)])
    pos_set = set([(x,y)])
    people_sum = grid[y][x]
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[ny][nx] and (l <= abs(grid[ny][nx] - grid[y][x]) <= r):
                visited[ny][nx] = True
                que.append((nx,ny))
                pos_set.add((nx,ny))
                people_sum += grid[ny][nx]
    return pos_set, people_sum
count = 0
while True:
    infos = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                pos_set, people_sum = bfs(x,y)
                pos_len = len(pos_set)
                if pos_len >= 2:
                    people_sum = people_sum//pos_len
                    infos.append((pos_set, people_sum))
    if not infos:
        break
    count += 1
    visited = [[False] * n for _ in range(n)]
    for pos_set, people_sum in infos:
        for x, y in pos_set:
            grid[y][x] = people_sum
print(count)