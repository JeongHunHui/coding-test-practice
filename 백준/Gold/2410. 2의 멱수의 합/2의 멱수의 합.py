# 00:11
n = int(input())

dp = [0] * (n + 1)
dp[0] = 1  # 0을 표현하는 경우는 1가지 (아무것도 사용하지 않는 경우)

num = 1 # 2의 제곱 수(2의 0 제곱 부터 시작)

# 각 2의 제곱 수 마다 dp[i]의 i를 만들 수 있는 경우의 수를 업데이트
while num <= n:
  for i in range(num, n + 1):
      dp[i] = (dp[i] + dp[i - num]) % 1000000000
  num *= 2

print(dp[n])