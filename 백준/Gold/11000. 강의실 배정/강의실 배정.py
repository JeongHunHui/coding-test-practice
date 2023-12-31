# 10:12
import heapq
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key = lambda x: x[0], reverse = True)
heap = [info.pop()[1]]
while info:
    start, finish = info.pop()
    if heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, finish)
print(len(heap))