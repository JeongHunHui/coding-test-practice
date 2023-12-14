# 22:43
n, k = map(int, input().split())
# 가치가 같은 동전이 여러 번 주어질 수도 있다.
coins = set([int(input()) for _ in range(n)])

# 동전을 최대한 적게 사용해서 k원이 되는 경우의 수 구하기
# 동전 1개 쓰기 -> 1, 5, 12
# 동전 2개 쓰기 -> 1+1, 5+1, 12+1, 5+5, 5+12, 12+12 -> 1개 쓴거 + 1개 쓴거
              # 즉, 2, 6, 10, 13, 17, 24
# 동전 3개 쓰기 -> 1개 쓴거 + 2개 쓴거
              # 2+1,
# 동전 4개 쓰기 -> 1개 쓴거 + 3개 쓴거
# -> d[i] = d[i-1]+d[1]

dp = [set([0])]
i = 1
answer = -1
while True:
  value_set = set()
  find_answer = False
  for coin in coins:
    for val in dp[i-1]:
      new_value = val + coin
      if new_value == k:
        answer = i
        break
      if new_value > k:
        continue
      value_set.add(new_value)
  if len(value_set) == 0 or answer != -1:
    break
  dp.append(value_set)
  i += 1

print(answer)