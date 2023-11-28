def solution(n, computers):
    def dfs(y):
        computers[y][y] = 2
        for x in range(n):
            if computers[y][x] == 1:
                computers[y][x] = 2
                computers[x][y] = 2
                dfs(x)
    answer = 0
    for y in range(n):
        if computers[y][y] == 1:
            answer += 1
            dfs(y)
    return answer