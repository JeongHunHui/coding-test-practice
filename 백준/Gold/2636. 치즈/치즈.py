# 21:58
from collections import deque
y_len, x_len = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(y_len)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs():
  visited = [[False] * x_len for _ in range(y_len)]
  visited[0][0] = True
  q = deque([(0,0)])
  count = 0
  while q:
    x, y = q.popleft()
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if nx >= 0 and nx < x_len and ny >= 0 and ny < y_len and not visited[ny][nx]:
        visited[ny][nx] = True
        if cheese[ny][nx] == 0:
          q.append((nx, ny))
        else:
          cheese[ny][nx] = 0
          count += 1
  return count

time = 0
pre_count = 0
while True:
  count = bfs()
  if count == 0:
    break
  time += 1
  pre_count = count
print(time)
print(pre_count)