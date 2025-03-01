# 23:52
# r: 세로 길이, c: 가로 길이, k: 거리
# -> 거리가 k인 집에 돌아가는 경우의 수
r,c,k = map(int, input().split())
graph = [[c == '.' for c in input()] for _ in range(r)]

from collections import deque

start_x, start_y = 0, r-1
des_x, des_y = c-1, 0
directions = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0

dq = deque([(start_x, start_y, 1, set([(start_x, start_y)]))])
while dq:
  x, y, distance, is_visited = dq.popleft()
  if distance == k:
    if x == des_x and y == des_y:
      answer += 1
    continue
  for dx, dy in directions:
    nx, ny = x+dx, y+dy
    if 0 <= nx < c and 0 <= ny < r and (nx, ny) not in is_visited and graph[ny][nx]:
      dq.append((nx, ny, distance+1, is_visited.union(set([(nx, ny)]))))
print(answer)