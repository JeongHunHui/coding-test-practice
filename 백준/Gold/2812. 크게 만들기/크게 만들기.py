# 23:12
n, k = map(int, input().split())
nums = [int(c) for c in input()]
stack = [nums[0]]
i, count = 1, k
while n-i >= count > 0:
  num = nums[i]
  if not stack or stack[-1] >= num:
    stack.append(num)
    i += 1
  else:
    stack.pop()
    count -= 1
print(''.join(map(str, stack + nums[i:]))[:n-k])