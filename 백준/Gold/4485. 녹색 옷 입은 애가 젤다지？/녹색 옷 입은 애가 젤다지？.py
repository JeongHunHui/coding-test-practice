# 02:11
from collections import deque
import math

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def find_min_cost(n, cave):
  que = deque()
  que.append([0,0])
  cost = [[math.inf]*n for _ in range(n)]
  cost[0][0] = cave[0][0]
  answer = math.inf
  while que:
    x,y = que.popleft()
    if x == n-1 and y == n-1:
      answer = min(cost[y][x], answer)
      continue
    for dx, dy in dirs:
      nx, ny = x+dx, y+dy
      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
      current_cost = cost[y][x] + cave[ny][nx]
      if cost[ny][nx] > current_cost:
        cost[ny][nx] = current_cost
        que.append([nx,ny])
  return answer

answers = []
n = int(input())
while n > 0:
  cave = []
  for _ in range(n):
    cave.append(list(map(int, input().split())))
  answers.append(find_min_cost(n, cave))
  n = int(input())

for i, answer in enumerate(answers):
  print(f'Problem {i+1}: {answer}')