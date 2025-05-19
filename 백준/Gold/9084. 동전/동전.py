# 10:50
t = int(input())
tc_list = []
for _ in range(t):
  n = int(input())
  coins = reversed(list(map(int, input().split())))
  target_money = int(input())
  tc_list.append((n, coins, target_money))

# n = 동전 금액
# coins[i] = n
# j = 목표 금액
# dp[i][j] = n원 이하의 동전만 써서 j원을 달성하는 경우의 수
# dp[i][j] = dp[i][j-n] + dp[i-1][j]

for n, coins, target_money in tc_list:
  dp = [[0]*(target_money + 1) for _ in range(n+1)]
  for i in range(1, n+1):
    dp[i][0] = 1
  for i, coin in enumerate(coins):
    i += 1
    for current_money in range(1, target_money+1):
      temp = dp[i-1][current_money]
      if current_money - coin >= 0:
        temp += dp[i][current_money-coin]
      dp[i][current_money] = temp
  print(dp[n][target_money])

      


  
  

#    0 1 2 3 4 5 6 7 8 9 10 11
#  0 1 0 0 0 0 0 0 0 0 0 0  0
#  1 1 1 1 1 1 1 1 1 1 1 1  1
#  5 1 1 1 1 1 2 1 1 1 1 3  1
# 10 1 1 1 1 1 2 2 2 2 2 4  4