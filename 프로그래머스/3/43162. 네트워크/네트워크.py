def solution(n, computers):
    def dfs(i):
        # 방문 표시
        computers[i][i] = 2
        # i번 노드에서 갈 수 있는 다른 노드 탐색
        for j in range(n):
            if computers[i][j] == 1:
                computers[i][j] = 2
                computers[j][i] = 2
                dfs(j)
    count = 0
    for i in range(n):
        # 아직 방문하지 않은 노드 방문 시 count 증가, 해당 노드 탐색
        if computers[i][i] == 1:
            count += 1
            dfs(i)
    return count