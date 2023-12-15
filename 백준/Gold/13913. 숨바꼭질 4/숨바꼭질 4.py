# 01:00
# 걸으면 x-1 or x+1
# 순간이동은 2*x로 이동
from collections import deque

n, k = map(int, input().split())
l = max(n, k) * 2

visited = [False] * (l + 1)
visited[n] = True

# bfs 수행
que = deque([[n,0,str(n)]])
while que:
  x, count, path = que.popleft()
  if x == k:
    print(count)
    print(path)
    break
  right_x = x+1
  if right_x <= l and not visited[right_x]:
    visited[right_x] = True
    que.append([right_x, count+1, path+" "+str(right_x)])
  left_x = x-1
  if left_x >= 0 and not visited[left_x]:
    visited[left_x] = True
    que.append([left_x, count+1, path+" "+str(left_x)])
  teleport_x = x*2
  if teleport_x <= l and not visited[teleport_x]:
    visited[teleport_x] = True
    que.append([teleport_x, count+1, path+" "+str(teleport_x)])