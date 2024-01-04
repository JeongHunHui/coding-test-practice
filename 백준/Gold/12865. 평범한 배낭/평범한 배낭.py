# 16:00
n, k = map(int, input().split())
things = [(0,0)]+[tuple(map(int, input().split())) for _ in range(n)]
# dp[i][j] = 1번 부터 i번 까지의 물건을 최대 무게가 j인 가방에 넣었을 때 최대 가치
# w: 현재 넣을 물건의 무게, v: 현재 넣을 물건의 가치
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    w, v = things[i]
    for j in range(1, k+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])