# 00:39
n, m = map(int, input().split())
grid = [[False]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    grid[a-1][b-1] = True
    grid[b-1][a-1] = True

visited = [False]*n
def dfs(i):
    visited[i] = True
    for j in range(n):
        if grid[i][j] and not visited[j]:
            dfs(j)

answer = 0
for i in range(n):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)