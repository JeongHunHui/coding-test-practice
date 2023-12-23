# 01:43
# 정점 수, 간선 수, 정점 번호
from collections import defaultdict, deque
n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for key in graph.keys():
  graph[key].sort()

answer1 = []
visited = [False]*(n+1)
visited[v] = True
def dfs(num):
  answer1.append(num)
  for key in graph[num]:
    if not visited[key]:
      visited[key] = True
      dfs(key)
dfs(v)

visited = [False]*(n+1)
visited[v] = True
que = deque([v])
answer2 = []
while que:
  num = que.popleft()
  answer2.append(num)
  visited[num] = True
  for key in graph[num]:
    if not visited[key]:
      que.append(key)
      visited[key] = True

print(' '.join(map(str, answer1)))
print(' '.join(map(str, answer2)))