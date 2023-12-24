# 13:00
n = int(input())
CONST = 15746

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
  dp[i] = (dp[i-1]+dp[i-2])%CONST
print(dp[n])