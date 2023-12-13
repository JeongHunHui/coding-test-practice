# 23:32
n = int(input())

x_set = set()
diagonal_set = set()
anti_diagonal_set = set()

answer = 0
def backtracking(y):
  global answer
  if y == n:
    answer += 1
    return
  for x in range(n):
    if x not in x_set and x-y not in diagonal_set and x+y not in anti_diagonal_set:
      x_set.add(x)
      diagonal_set.add(x-y)
      anti_diagonal_set.add(x+y)
      backtracking(y+1)
      x_set.remove(x)
      diagonal_set.remove(x-y)
      anti_diagonal_set.remove(x+y)
backtracking(0)
print(answer)