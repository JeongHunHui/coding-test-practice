# 22:15
t, w = map(int, input().split())
nums = [0]+[int(input()) for _ in range(t)]

# i초에서 j번 움직였을 때 자두의 최대 개수 -> dp[i][j]
# -> i초에서 j번 움직였다면, 이전 상태는 i-1초때 j번 움직였거나 j-1번 움직인 상태
# -> dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + (지금 자두 받았으면 +1)
dp = [[0]*(w+1) for _ in range(t+1)]

# 1초 때 한번 움직인 경우와 한번도 움직이지 않은 경우를 설정
dp[1][0], dp[1][1] = nums[1] % 2, nums[1] // 2

for i in range(2, t+1):
  dp[i][0] = dp[i-1][0] + (1 if nums[i] == 1 else 0)

for i in range(2, t+1):
  for j in range(1, w+1):
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + (1 if nums[i] == (j%2+1) else 0)
print(max(dp[t]))