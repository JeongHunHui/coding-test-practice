# 00:12
n = int(input())
burgers = [int(burger) for burger in input().split()]
dp = set()
dp.add(tuple([0,0,0]))
for burger in burgers:
  new_dp = set()
  for v in dp:
    for i in range(3):
      temp = list(v)
      temp[i] += burger
      new_dp.add(tuple(sorted(temp)))
  dp = new_dp
print(max([min(v) for v in dp]))