# 12:39
import heapq
infos = [tuple(map(int, input().split())) for _ in range(int(input()))]
infos.sort(key=lambda x: x[0], reverse=True)
heap = [infos.pop()[1]]
while infos:
    start, finish = infos.pop()
    if heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, finish)
print(len(heap))