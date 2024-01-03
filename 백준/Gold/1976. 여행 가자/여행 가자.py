# 15:47
from collections import deque
n = int(input())
m = int(input())
grid = [[0]*(n+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
def can_visited(plan):
    if len(plan) >= 2 and set(plan) == 1:
        return False
    plan = set(plan)
    start = plan.pop()
    que = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    while que and plan:
        num = que.popleft()
        for i in range(1, n+1):
            if grid[num][i] == 1 and not visited[i]:
                que.append(i)
                visited[i] = True
                if i in plan:
                    plan.remove(i)
    return False if plan else True
if can_visited(plan):
    print('YES')
else:
    print('NO')