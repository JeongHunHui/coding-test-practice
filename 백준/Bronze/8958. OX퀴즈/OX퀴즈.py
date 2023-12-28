# 17:36
n = int(input())
tc_list = [[c for c in input()] for _ in range(n)]
def calculate_score(tc):
  score = 0
  temp = 1
  for c in tc:
    if c == 'O':
      score += temp
      temp += 1
    else:
      temp = 1
  return score
for tc in tc_list:
  print(calculate_score(tc))