# 18:39
import heapq

def solution(n, s, a, b, fares):
    # n = 정점 수
    # s = 출발 지점
    # a = A의 도착 지점
    # b = B의 도착 지점
    # fares = [지점1, 지점2, 요금]
    
    graph = [[-1]*(n+1) for _ in range(n+1)]
    for d1, d2, fare in fares:
        graph[d1][d2] = fare
        graph[d2][d1] = fare
    
    # 다익스트라로 시작지점 부타 각 지점까지의 최단 거리
    def min_dist(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)] # 거리, 시작 지점
    
        while pq:
            distance, num = heapq.heappop(pq)
            
            # 이미 구한 최단 거리보다 낮으면 컷
            if dist[num] < distance:
                continue
        
            for n_num, n_distance in enumerate(graph[num]):
                if n_num == 0 or n_distance == -1:
                    continue
                t_distance = distance + n_distance
                if t_distance < dist[n_num]:
                    dist[n_num] = t_distance
                    heapq.heappush(pq, (t_distance, n_num))
        return dist
    
    s_min_dist = min_dist(s)
    a_min_dist = min_dist(a)
    b_min_dist = min_dist(b)
    
    answer = float('inf')
    
    # 최단 거리 구하기
    # 1. 합승 O
        # 1-1 끝까지 합승 -> s-a 최단 + a-b 최단
        # 1-2 중간에 따로 -> s-? 최단 + ?-a 최단 + ?-b 최단
    # 2. 합승 X
    
    # s-i + i-a + i-b 구하기
    # 이때, i=a or i=b면 끝까지 합승(1-1), i=s면 합승 X(2), 나머진 중간에 따로(1-2)
    for i in range(1, n + 1):
        total_cost = s_min_dist[i] + a_min_dist[i] + b_min_dist[i]
        answer = min(answer, total_cost)
    
    return answer