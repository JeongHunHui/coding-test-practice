# 14:29
n = int(input())
CONST = 9901
# dp[i][j] 세로가 i칸이고 사자를 j마리 놓는 경우의수
dp = [1]*(n+1)
dp[1] = 3
for i in range(2, n+1):
  dp[i] = (dp[i-1]*2 + dp[i-2])%9901
print(dp[-1])