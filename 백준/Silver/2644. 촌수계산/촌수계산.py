# 10:16
from collections import deque
n = int(input())
start, finish = map(int, input().split())
grid = [[False]*(n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    t1, t2 = map(int, input().split())
    grid[t1][t2] = True
    grid[t2][t1] = True
visited = [False]*(n+1)
que = deque([(start,0)])
visited[start] = True
answer = -1
while que:
    num, depth = que.popleft()
    if num == finish:
        answer = depth
        break
    for i in range(1, n+1):
        if grid[num][i] and not visited[i]:
            que.append((i, depth+1))
            visited[i] = True
print(answer)