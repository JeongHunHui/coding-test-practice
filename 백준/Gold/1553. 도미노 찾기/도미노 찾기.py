# 23:56
from collections import defaultdict

dominos = [[int(i) for i in input()] for _ in range(8)]

is_domino_used = defaultdict(lambda: False)

is_visited = [[False for _ in range(7)] for _ in range(8)]

answer = 0

def backtracking(x, y):
  global answer
  if x == 7:
    if y == 7:
      answer += 1
    else:
      backtracking(0, y+1)
  elif is_visited[y][x]:
    backtracking(x+1, y)
  else:
    current = dominos[y][x]
    is_visited[y][x] = True
    if y <= 6 and not is_visited[y+1][x]:
      bottom = dominos[y+1][x]
      new_domino = (bottom, current) if current > bottom else (current, bottom)
      if not is_domino_used[new_domino]:
        is_visited[y+1][x] = True
        is_domino_used[new_domino] = True
        backtracking(x+1, y)
        is_visited[y+1][x] = False
        is_domino_used[new_domino] = False
    if x <= 5 and not is_visited[y][x+1]:
      right = dominos[y][x+1]
      new_domino = (right, current) if current > right else (current, right)
      if not is_domino_used[new_domino]:
        is_visited[y][x+1] = True
        is_domino_used[new_domino] = True
        backtracking(x+2, y)
        is_visited[y][x+1] = False
        is_domino_used[new_domino] = False
    is_visited[y][x] = False
  
backtracking(0,0)

print(answer)