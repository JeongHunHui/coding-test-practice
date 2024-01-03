# 16:36
import heapq
n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
answer = 0
while len(heap) >= 2:
    n1, n2 = heapq.heappop(heap), heapq.heappop(heap)
    s = n1 + n2
    answer += s
    heapq.heappush(heap, s)
print(answer)