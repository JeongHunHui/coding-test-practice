# 01:47
n = int(input())
adj_list = [[] for _ in range(n+1)]

for _ in range(n-1):
  u, v = map(int, input().split())
  adj_list[u].append(v)
  adj_list[v].append(u)
  
leaf_nodes = []
for i, nodes in enumerate(adj_list):
  if len(nodes) == 1:
    leaf_nodes.append(i)

answer = 0

# 리프노드가 없으면 끝
while leaf_nodes:
  leaf_node = leaf_nodes.pop()
  # 부모노드가 존재하면
  if adj_list[leaf_node]:
    parent_node = adj_list[leaf_node][0]
    # 부모노드와 다른 노드와의 연결 삭제
    for node in adj_list[parent_node]:
      adj_list[node].remove(parent_node)
      # 부모노드와 인접한 다른 노드와 연결된 노드가 1개면 리프노드에 추가
      if len(adj_list[node]) == 1:
        leaf_nodes.append(node)
      # 리프노드와 부모노드 제거
      adj_list[parent_node] = []
    answer += 1
    adj_list[leaf_node] = []

print(answer)