import math, heapq

def solution(n, edge):
    node_dict = {i:[] for i in range(n)}
    for i, j in edge:
        node_dict[i-1].append((j-1,1))
        node_dict[j-1].append((i-1,1))
    
    # start에서 다른 노드들로 가는 최단 거리들을 list로 반환
    def dijkstra(start):
        start -= 1
        heap = []
        heapq.heappush(heap, (0, start))
        # start에서 0 ~ n-1 노드까지 이동거리
        # 우선 무한대로 선언한 뒤 탐색을 진행하며 최솟값으로 업데이트
        distances = [math.inf] * n
        # start에서 start까지는 거리가 0
        distances[start] = 0
        
        while heap:
            distance, node = heapq.heappop(heap)
            # node와 연결된 다른 노드(new_node)로 가는 경로 탐색
            for new_node, d in node_dict[node]:
                # start~node의 거리가 현재 최단 경로보다 크거나 같으면 스킵
                if distance >= distances[new_node]:
                    continue
                # start~node + node~new_node
                new_distance = distance + d
                # 새로운 경로가 현재 최단 경로보다 작으면 업데이트, heap에 push
                if new_distance < distances[new_node]:
                    distances[new_node] = new_distance
                    heapq.heappush(heap, (new_distance, new_node))
        return distances
            
    distances = dijkstra(1)
    
    max_dist = 0
    answer = 0
    for dist in distances:
        if dist == max_dist:
            answer += 1
            continue
        if dist > max_dist:
            answer = 1
            max_dist = dist
        
    return answer