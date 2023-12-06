# 23:13
n = int(input())
nums = [int(input()) for _ in range(n)]

def search(key):
  key_set = set([key])
  value_set = set()
  while True:
    value = nums[key-1]
    value_set.add(value)
    if value in key_set or key == value:
      break
    key_set.add(value)
    key = value
  return key_set if key_set == value_set else set()

answer = set()
for key in nums:
  answer = answer | search(key)
  
print(len(answer))
for num in sorted(list(answer)):
  print(num)