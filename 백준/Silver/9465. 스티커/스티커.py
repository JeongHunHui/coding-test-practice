# 14:15
t = int(input())
tcs = []
for _ in range(t):
    n = int(input())
    tc = [list(map(int, input().split())) for _ in range(2)]
    tcs.append((n, tc))
def calculate_max_score(n, stickers):
    # 이전 단계에서 위 dp[i][0], 아래 dp[i][1], X dp[i][2]
    # dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + up_v
    # dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + down_v
    # dp[i][2] = max(dp[i-1][0], dp[i-1][1])
    dp = [[0]*3 for _ in range(n)]
    dp[0] = [stickers[0][0], stickers[1][0], 0]
    for i in range(1, n):
        up_value = stickers[0][i]
        down_value = stickers[1][i]
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + up_value
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + down_value
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])
    return max(dp[n-1])
for n, stickers in tcs:
    print(calculate_max_score(n, stickers))