# 21:21
# 온전한 알약 수 = i, 절반남은 알약 수 = j 일때 만들 수 있는 문자열의 수 -> dp[i][j]
# 온전한 알약이 2개, 절반남은 알약이 2개 있다고 가정
# 선택할 수 있는 행동은 온전한 알약을 먹고 절반 알약 1개 추가 or 절반 알약 먹기
# 즉, 1,3 or 2,1 -> 2,2 일때 경우의 수는 1,3의 경우의 수 + 2,1의 경우의 수
# -> dp[i][j] = dp[i-1][j+1] + dp[i][j-1] (단, j>0)
# -> dp[i][0] = dp[i-1][1] (j가 0이면 온전한 알약을 먹는 경우의 수 밖에 없기 때문)
# -> dp[0][j] = 1 (i가 0이면 절반 알약을 먹는 경우의 수 밖에 없기 때문)

# 알약의 수는 최대 30
dp = [[0]*31 for _ in range(31)]

# 반쪽짜리 알약만 있는 경우는 무조건 1
for i in range(1, 31):
  dp[0][i] = 1

for i in range(1, 31):
  # 반쪽짜리 알약이 없는 경우
  dp[i][0] = dp[i-1][1]
  for j in range(1, 31-i):
    dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

inputs = []
while True:
  n = int(input())
  if n == 0:
    break
  inputs.append(n)

for inp in inputs:
  print(dp[inp][0])