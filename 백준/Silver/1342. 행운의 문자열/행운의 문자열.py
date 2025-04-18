# 23:42
from collections import Counter

s = input()
l = len(s)
counter = Counter(s)
answer = 0

s_set = set()

def backtracking(s):
  global answer
  depth = len(s)
  if depth == l and s not in s_set:
    s_set.add(s)
    answer += 1
    return
  for c in counter:
    if (depth == 0 or s[-1] != c) and counter[c] > 0:
      counter[c] -= 1
      backtracking(s + c)
      counter[c] += 1

backtracking('')
print(answer)