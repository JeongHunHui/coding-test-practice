def solution(n, computers):
    visited = [False]*n
    answer = 0
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if j != i and not visited[j] and computers[i][j] == 1:
                dfs(j)
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer