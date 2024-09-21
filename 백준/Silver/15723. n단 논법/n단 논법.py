# 19:47
from collections import defaultdict

n = int(input())
premises = [input().split(" is ") for _ in range(n)]
m = int(input())
queries = [input().split(" is ") for _ in range(m)]

def build_graph(premises):
    graph = defaultdict(set)
    for a, b in premises:
        graph[a].add(b)
    return graph

def can_reach(graph, start, end, visited):
    if start == end:
        return True
    if start in visited:
        return False
    visited.add(start)
    for neighbor in graph[start]:
        if can_reach(graph, neighbor, end, visited):
            return True
    return False

graph = build_graph(premises)
results = []
for a, b in queries:
    if can_reach(graph, a, b, set()):
        results.append("T")
    else:
        results.append("F")
print("\n".join(results))
