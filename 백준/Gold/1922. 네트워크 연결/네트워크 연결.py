# 13:55
import heapq

n = int(input())
m = int(input())
heap = []
for _ in range(m):
  i, j, weight = map(int, input().split())
  heapq.heappush(heap, [weight, (i, j)])

disjoint_set_list = []
total_weight = 0

while heap:
  if len(disjoint_set_list) > 0 and len(disjoint_set_list[0]) == n:
    break
  weight, edge = heapq.heappop(heap)
  i, j = edge
  if i == j:
    continue
  i_index, j_index = None, None
  for index, disjoint_set in enumerate(disjoint_set_list):
    # 들어갈 집합을 찾았으면 break
    if i_index != None and j_index != None:
      break
    # 들어갈 집합의 인덱스를 저장
    if i in disjoint_set:
      i_index = index
    if j in disjoint_set:
      j_index = index
  
  # node i와 j가 기존 집합에 속하면
  if i_index != None and j_index != None:
    # i와 j가 서로 같은 집합에 속하면 continue
    if i_index == j_index:
      continue
    # i와 j가 서로 다른 집합에 속하면 두 집합을 합집합
    disjoint_set_list[i_index] = disjoint_set_list[i_index] | disjoint_set_list[j_index]
    del disjoint_set_list[j_index]
  # i가 속하는 집합이 있으면 j도 i가 속한 집합에 추가
  elif i_index != None:
    disjoint_set_list[i_index].add(j)
  # j가 속하는 집합이 있으면 i도 j가 속한 집합에 추가
  elif j_index != None:
    disjoint_set_list[j_index].add(i)
  # i와 j가 속하는 집합이 없으면 새 집합을 생성
  else:
    disjoint_set_list.append(set([i, j]))
  # 비용 추가
  total_weight += weight

print(total_weight)