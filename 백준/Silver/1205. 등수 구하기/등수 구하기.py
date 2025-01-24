# 11:35
n, my_score, p = map(int, input().split())
scores = []
if n > 0:
  scores = list(map(int, input().split()))

def get_rank(scores, my_score, p):
  rank = 0
  pre_score = float('inf')
  scores += [-1]
  for i, score in enumerate(scores):
    if i == p:
      return -1
    if my_score > score:
      if my_score == pre_score:
        return rank
      return i+1
    if pre_score > score:
      rank = i+1
      pre_score = score
  return -1

print(get_rank(scores, my_score, p))