# 14:59
from collections import deque

n = int(input())
visited = set([1])
que = deque([(1,0)])
while que:
  num, depth = que.popleft()
  if num == n:
    print(depth)
    break
  triple = num*3
  if triple not in visited and triple <= n:
    que.append((triple, depth+1))
    visited.add(triple)
  double = num*2
  if double not in visited and double <= n:
    que.append((double, depth+1))
    visited.add(double)
  plus = num+1
  if plus not in visited and plus <= n:
    que.append((plus, depth+1))
    visited.add(plus)