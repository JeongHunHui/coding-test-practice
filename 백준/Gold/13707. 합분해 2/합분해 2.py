# 02:18
n, k = map(int, input().split())
# 0 부터 n까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수
# 덧셈의 순서가 바뀐 경우는 다른 경우
# ex) 1+2와 2+1은 다른 경우임
# 한 개의 수를 여러번 쓸 수 있음

# 표 그려봤는데 규칙 바로 보임
# dp[n][k] = dp[n-1][k] + dp[n][k-1]
# 메모리 초과나서 계획 변경

dp = [1]*(k+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, k+1):
        dp[j] = (dp[j] + dp[j-1])%1000000000
print(dp[k])