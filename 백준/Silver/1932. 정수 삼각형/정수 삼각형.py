# 01:41
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*len(triangle[i]) for i in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
  l = len(dp[i])
  for j in range(l):
    max_val = None
    if j == l-1:
      max_val = dp[i-1][j-1]
    elif j == 0:
      max_val = dp[i-1][j]
    else:
      max_val = max(dp[i-1][j], dp[i-1][j-1])
    dp[i][j] = max_val + triangle[i][j]
print(max(dp[n-1]))