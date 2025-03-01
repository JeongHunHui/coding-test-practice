# 01:02
import heapq as hq

n,m,x=map(int, input().split())
graph = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
  a,b,t=map(int, input().split())
  graph[a-1][b-1]=t
is_visited = [False]*n

def daik(start, graph):
  nodes = []
  hq.heappush(nodes, (0, start))
  distances = [float('inf')]*n
  distances[start] = 0
  while nodes:
    distance, start = hq.heappop(nodes)
    for destination in range(n):
      new_distance = graph[start][destination]
      if new_distance != float('inf') and distances[destination] > distance+new_distance:
        distances[destination] = distance+new_distance
        hq.heappush(nodes, (distances[destination], destination))
  return distances

x_to_all_distances = daik(x-1, graph)

reverse_graph = [[float('inf')]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    reverse_graph[i][j] = graph[j][i]

all_to_x_distances = daik(x-1, reverse_graph)

answer = 0
for i in range(n):
  i_to_x = all_to_x_distances[i]
  x_to_i = x_to_all_distances[i]
  answer = max(answer, i_to_x + x_to_i)

print(answer)