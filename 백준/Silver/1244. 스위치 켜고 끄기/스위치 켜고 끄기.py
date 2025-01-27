# 남학생은 배수들 변경
# 여학생은 대칭 & 인접 변경

switch_count = int(input())
switches = list(map(int, input().split()))
student_count = int(input())
students = [list(map(int, input().split())) for _ in range(student_count)]

def get_male_switch_nums(switch_num):
  nums = []
  num = switch_num
  while num <= switch_count:
    nums.append(num)
    num += switch_num
  return nums

def get_female_switch_nums(switch_num):
  nums = [switch_num]
  range_num = 1
  while True:
    a = switch_num - range_num
    b = switch_num + range_num
    if a <= 0 or a > switch_count or b <= 0 or b > switch_count:
      break
    if switches[a-1] != switches[b-1]:
      break
    nums.append(a)
    nums.append(b)
    range_num += 1
  return nums

for gender, switch_num in students:
  switch_nums = get_male_switch_nums(switch_num) if gender == 1 else get_female_switch_nums(switch_num)
  for num in switch_nums:
    switches[num-1] = (switches[num-1] + 1) % 2

for i in range(0, len(switches), 20):
  print(" ".join(map(str, switches[i:i + 20])))