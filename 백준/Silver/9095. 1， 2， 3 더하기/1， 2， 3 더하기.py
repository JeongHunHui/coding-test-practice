# 16:38
t = int(input())
tc_list = [int(input()) for _ in range(t)]

# dp[i][j] 숫자 j개를 써서 i를 만드는 경우의 수
# dp[i][j] = dp[i-1][j-1] dp[i-2][j-1] dp[i-3][j-1]
dp = [[0] * 11 for _ in range(11)]

dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1
dp[2][2] = 1

for j in range(2, 11):
  for i in range(3, 11):
    dp[i][j] = dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]

for tc in tc_list:
  print(sum(dp[tc]))