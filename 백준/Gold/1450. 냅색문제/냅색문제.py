# 04:24
n, c = map(int, input().split())
weights = list(map(int, input().split()))

left_weights, right_weights = weights[:n//2], weights[n//2:]
left_sums, right_sums = [], []

def dfs(weights, current, i, sum_list):
  if current > c:
    return
  if i >= len(weights):
    sum_list.append(current)
    return
  dfs(weights, current+weights[i], i+1, sum_list)
  dfs(weights, current, i+1, sum_list)

dfs(left_weights, 0, 0, left_sums)
dfs(right_weights, 0, 0, right_sums)
right_sums.sort()

answer = 0
for num in left_sums:
  # 배낭의 남은 무게
  target = c - num
  start = 0
  end = len(right_sums)
  # 배낭의 남은 무게보다 낮은 무게 합의 수를 이진 탐색으로 구한다.
  # target 이하 무게 합의 수를 구하려면 target이하인 것 중 가장 오른쪽 포인터를 알아야함
  while start < end:
    mid = (start + end) // 2
    if right_sums[mid] > target:
      end = mid
    else:
      start = mid+1
  answer += end

print(answer)