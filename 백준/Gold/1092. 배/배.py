# 13:30
# 크레인 수
n = int(input())
# 각 크레인의 무게 제한
limits = list(map(int, input().split()))
# 박스 수
m = int(input())
# 각 박스의 무게
box_weights = list(map(int, input().split()))

limits.sort(reverse=True)
box_weights.sort(reverse=True)

answer = 0
while box_weights:
  box_num = 0
  crane_num = 0
  answer += 1
  while crane_num < n and box_num < len(box_weights):
    if limits[crane_num] >= box_weights[box_num]:
      del box_weights[box_num]
      crane_num += 1
    else:
      box_num += 1
  if crane_num == 0:
    answer = -1
    break

print(answer)