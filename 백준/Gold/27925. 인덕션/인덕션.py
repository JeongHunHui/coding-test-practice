# 21:52
# 온도는 초기값 = 0, 0~9, 9에서 + > 0, 0에서 - > 9
# N개의 음식을 요리 하는 데 누르는 버튼 횟수의 최솟값
from collections import defaultdict
n = int(input())
foods = [int(food_temp) for food_temp in input().split()]

dp = defaultdict(lambda: float('inf'))
dp[tuple([0,0,0])] = 0

for j, food in enumerate(foods):
  new_dp = defaultdict(lambda: float('inf'))
  for inductions, count in dp.items():
    for i, induction in enumerate(inductions):
      diff = abs(food - induction)
      min_diff = min(diff, 10 - diff)
      temp = [v for v in inductions]
      temp[i] = (temp[i] + min_diff) % 10 if (food - temp[i]) % 10 < 5 else (temp[i] - min_diff) % 10
      new_inductions = tuple(temp)
      new_dp[new_inductions] = min(new_dp[new_inductions], count + min_diff)
  dp = new_dp
print(min(dp.values()))