# 15:14
n = int(input())
nums = list(map(int, input().split()))

# 이거는 꺼꾸로 하면 될듯?
# 나누기/2 or -1을 해서 0으로 만들어야하는거임
# 1. 전체를 짝수로 만듦
# 2. 나누기 2 박음
# 3. 모든 수가 0이 될 때 까지 반복

answer = 0

# 모든 수가 0이 될 때 까지
while True:
  count = 0
  new_nums = []
  for num in nums:
    if num != 0 and num % 2 != 0:
      count += 1
      new_nums.append(num-1)
    else:
      new_nums.append(num)
  answer += count
  if all(num == 0 for num in new_nums):
    break
  nums = [num/2 if num != 0 else 0 for num in new_nums]
  answer += 1

print(answer)