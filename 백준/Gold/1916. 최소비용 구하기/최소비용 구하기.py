# 01:21
import math, heapq

n = int(input())
m = int(input())
graph = [[math.inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
  i, j, weight = map(int, input().split())
  graph[i][j] = min(graph[i][j], weight)
start, end = map(int, input().split())

answer = math.inf

def dijkstra(start):
  global answer
  heap = []
  heapq.heappush(heap, [0,start])
  distances = [math.inf]*(n+1)
  while heap:
    weight, num = heapq.heappop(heap)
    if num == end:
      answer = min(weight, answer)
      continue
    if weight > distances[num]:
      continue
    for i in range(1,n+1):
      if graph[num][i] + weight < distances[i]:
        distances[i] = graph[num][i] + weight
        heapq.heappush(heap, [graph[num][i] + weight, i])

dijkstra(start)

print(answer)