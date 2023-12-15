# 00:31
t = int(input())
gears = [None]+[list(map(int, input())) for _ in range(t)]
k = int(input())
infos = [list(map(int, input().split())) for _ in range(k)]

def rotate(gear_num, is_clockwise):
  global gears
  if is_clockwise:
    gears[gear_num] = [gears[gear_num][-1]] + gears[gear_num][:-1]
  else:
    gears[gear_num] = gears[gear_num][1:] + [gears[gear_num][0]]

left_index = 6
right_index = 2

for gear_num, dir_num in infos:
  rotate_infos = [[gear_num, dir_num]]
  # 오른쪽 톱니 바퀴 검사
  temp_dir_num = dir_num
  for num in range(gear_num, t):
    if gears[num][right_index] == gears[num+1][left_index]:
      break
    temp_dir_num *= -1
    rotate_infos.append([num+1, temp_dir_num])
  # 왼쪽 톱니 바퀴 검사
  temp_dir_num = dir_num
  for num in range(gear_num, 1, -1):
    if gears[num][left_index] == gears[num-1][right_index]:
      break
    temp_dir_num *= -1
    rotate_infos.append([num-1, temp_dir_num])
  # 회전
  for i, j in rotate_infos:
    rotate(i, j==1)

print(sum([1 for gear in gears[1:] if gear[0] == 1]))