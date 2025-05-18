# 13:26
a, b = input().split()
min_len, max_len = len(a), len(b)

nums = []
def make_47_num(l, current_l, answer):
  if current_l > l:
    nums.append(int(answer))
    return
  make_47_num(l, current_l+1, answer+'4')
  make_47_num(l, current_l+1, answer+'7')


for l in range(min_len, max_len+1):
  make_47_num(l, 1, '')

min_num, max_num = int(a), int(b)
min_idx, max_idx = None, None
for i in range(len(nums)):
  num = nums[i]
  if num >= min_num:
    min_idx = i
    break
for i in range(len(nums)-1, -1, -1):
  num = nums[i]
  if num <= max_num:
    max_idx = i
    break

if min_idx == None or max_idx == None:
  print(0)
else:
  print(max_idx - min_idx + 1)