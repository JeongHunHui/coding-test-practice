# 22:05
# 2-친구 -> 친구의 친구면 친구임
# ex: A-B, B-C, B-D, D-E -> A는 3명(BCD), B는 4명(ACDE) C는 3명(BAD) D는 4명(EBCA) E는 2명(DB)
n = int(input())
graph = [[1 if c == 'Y' else float('inf') for c in input()] for _ in range(n)]
for i in range(n):
  graph[i][i] = 0


for k in range(n):
  for a in range(n):
    for b in range(n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(n):
  num = 0
  for distance in graph[i]:
    if distance in range(1, 3):
      num += 1
  answer = max(answer, num)

print(answer)