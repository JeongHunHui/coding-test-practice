# 20:16
from collections import deque
import math, copy
n = int(input())
min_num = math.inf
max_num = 0
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    min_num = min(min(row), min_num)
    max_num = max(max(row), max_num)
    grid.append(row)
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x, y, visited):
    visited[y][x] = False
    que = deque([(x,y)])
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[ny][nx]:
                visited[ny][nx] = False
                que.append((nx, ny))
answer = 1
can_visit = [[True] * n for _ in range(n)]
for i in range(min_num, max_num + 1):
    for y in range(n):
        for x in range(n):
            if grid[y][x] <= i:
                can_visit[y][x] = False
    visited = copy.deepcopy(can_visit)
    temp_answer = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                bfs(x,y,visited)
                temp_answer += 1
    answer = max(answer, temp_answer)
print(answer)