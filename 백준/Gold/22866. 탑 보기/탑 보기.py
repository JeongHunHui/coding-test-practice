# 08:00
import math
n = int(input())
buildings = [0]+list(map(int, input().split()))
counts = [0]*(n+1)
near_building = [math.inf]*(n+1)

def find_buildings():
  stack = []
  for i in range(1, n+1):
    h = buildings[i]
    while stack and stack[-1][1] <= h:
      stack.pop()
    counts[i] += len(stack)
    if stack and abs(stack[-1][0] - i) < abs(near_building[i] - i):
      near_building[i] = stack[-1][0]
    stack.append((i, h))
  stack = []
  for i in range(n, 0, -1):
    h = buildings[i]
    while stack and stack[-1][1] <= h:
      stack.pop()
    counts[i] += len(stack)
    if stack and abs(stack[-1][0] - i) < abs(near_building[i] - i):
      near_building[i] = stack[-1][0]
    stack.append((i, h))

find_buildings()
for i in range(1, n+1):
  count = counts[i]
  if count == 0:
    print(0)
    continue
  print(count, near_building[i])