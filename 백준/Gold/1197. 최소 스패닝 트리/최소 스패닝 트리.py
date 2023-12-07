# 16:06
from collections import defaultdict
import heapq

v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
  i, j, weight = map(int, input().split())
  graph[i].append([weight, j])
  graph[j].append([weight, i])

# heap에 시작 노드 추가
heap = [(0, 1)]
# 노드를 방문했는지 체크하는 list
is_visited = [False] * (v+1)
# 총 비용
total_weight = 0

while heap:
  weight, i = heapq.heappop(heap)
  if is_visited[i]:
    continue
  is_visited[i] = True
  total_weight += weight
  for j_weight, j in graph[i]:
    if not is_visited[j]:
      heapq.heappush(heap, (j_weight, j))

print(total_weight)