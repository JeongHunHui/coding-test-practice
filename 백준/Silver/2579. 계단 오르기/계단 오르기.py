# 15:18
# 계단의 수
n = int(input())
scores = [0]+[int(input()) for _ in range(n)]
# dp[i][j] = j번째 계단에서의 최대 점수 값
# i = 1칸 올라간 상태면 0, 2칸 올라간 상태면 1
dp = [[0] * (n+1) for i in range(2)]
dp[1][1] = scores[1]

for j in range(2, n+1):
  dp[0][j] = max(dp[0][j], dp[1][j-1]+scores[j])
  dp[1][j] = max(dp[1][j], max(dp[0][j-2], dp[1][j-2]) + scores[j])

print(max(dp[0][n], dp[1][n]))