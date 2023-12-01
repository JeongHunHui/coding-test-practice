from collections import defaultdict
import math, heapq

def solution(n, edge):
    node_dict = defaultdict(list)
    for i, j in edge:
        node_dict[i-1].append(j-1)
        node_dict[j-1].append(i-1)
    
    def dijkstra(start):
        # 1번 노드에서 각 노드까지의 최단경로를 저장할 list
        distances = [math.inf]*n
        distances[start] = 0
        heap = []
        heapq.heappush(heap, (start, 0))
        while heap:
            node, weight = heapq.heappop(heap)
            for i in node_dict[node]:
                if distances[i] > weight + 1:
                    distances[i] = weight + 1
                    heapq.heappush(heap, (i, weight+1))
        return distances
            
    distances = dijkstra(0)
    max_dist = max(distances)
    return sum([1 for d in distances if max_dist == d])
