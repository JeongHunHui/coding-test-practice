# 17:51
n = int(input())
money_list = list(map(int, input().split()))
total = int(input())
start, end = 0, max(money_list)
while start <= end:
  mid = (start + end) // 2
  current_total = sum([val if val < mid else mid for val in money_list])
  if current_total > total:
    end = mid - 1
  else:
    start = mid + 1
print(end)