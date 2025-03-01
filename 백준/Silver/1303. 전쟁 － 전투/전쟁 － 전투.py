# 00:38
from collections import deque

n,m=map(int, input().split())
soldiers = [[c for c in input()] for _ in range(m)]
is_visited = [[False]*n for _ in range(m)]

directions = [(0,1),(0,-1),(1,0),(-1,0)]
def search(x, y, soldier):
  answer = 0
  dq = deque([(x,y)])
  while dq:
    x, y = dq.popleft()
    answer += 1
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0<=nx<n and 0<=ny<m and not is_visited[ny][nx] and soldier == soldiers[ny][nx]:
        is_visited[ny][nx] = True
        dq.append((nx,ny))
  return answer * answer

b, w = 0, 0
for x in range(n):
  for y in range(m):
    if not is_visited[y][x]:
      soldier = soldiers[y][x]
      is_visited[y][x] = True
      num = search(x,y,soldier)
      if soldier == 'B':
        b += num
      else:
        w += num

print(w, b)