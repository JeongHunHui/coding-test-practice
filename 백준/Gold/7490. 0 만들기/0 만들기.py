# 16:38
tc_count = int(input())
tc_list = [int(input()) for _ in range(tc_count)]

answers = []
def dfs(expression, current, n, total, temp):
  if current > n:
    if total + int(temp) == 0:
      answers.append(expression)
    return
  # 공백 플러스 마이너스 순으로 출력
  dfs(f'{expression} {current}', current+1, n, total, f'{temp}{current}')
  dfs(f'{expression}+{current}', current+1, n, total+int(temp), f'{current}')
  dfs(f'{expression}-{current}', current+1, n, total+int(temp), f'-{current}')

dfs('1', 2, tc_list[0], 0, '1')
for answer in answers:
  print(answer)

for tc in tc_list[1:]:
  answers = []
  dfs('1', 2, tc, 0, '1')
  print()
  for answer in answers:
    print(answer)