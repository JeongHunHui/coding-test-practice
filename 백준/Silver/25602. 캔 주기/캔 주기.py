from copy import deepcopy

n, k = [int(i) for i in input().split()]
can_counts = [int(i) for i in input().split()]
r_happiness = [[int(i) for i in input().split()] for _ in range(k)]
m_happiness = [[int(i) for i in input().split()] for _ in range(k)]

max_val = 0

def dfs_r(result, depth, counts, happiness):
  if depth == k:
    dfs_m([], 0, deepcopy(counts), happiness)
    return
  for j in range(n):
    if counts[j] > 0:
      new_counts = deepcopy(counts)
      new_counts[j] -= 1
      new_happiness = happiness + r_happiness[depth][j]
      dfs_r(result + [j], depth + 1, new_counts, new_happiness)

def dfs_m(result, depth, counts, happiness):
  global max_val  # 전역 변수로 max_val 사용
  if depth == k:
    max_val = max(max_val, happiness)
    return
  for j in range(n):
    if counts[j] > 0:
      new_counts = deepcopy(counts)
      new_counts[j] -= 1
      new_happiness = happiness + m_happiness[depth][j]
      dfs_m(result + [j], depth + 1, new_counts, new_happiness)

dfs_r([], 0, deepcopy(can_counts), 0)

print(max_val)