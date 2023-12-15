# 01:41
from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(set)
degrees = [0]*(n+1)
degrees[0] = -1
for _ in range(m):
  first, second = map(int, input().split())
  graph[first].add(second)
  degrees[second] += 1

def get_leafs():
  return [i for i in range(1,n+1) if degrees[i] == 0]

answer = []
que = deque(get_leafs())
while que:
  node = que.popleft()
  answer.append(str(node))
  for new_node in graph[node]:
    degrees[new_node] -= 1
  degrees[node] = -1
  if not que:
    for leaf in get_leafs():
      que.append(leaf)

print(' '.join(answer))