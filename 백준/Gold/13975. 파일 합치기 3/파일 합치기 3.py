# 15:23
import heapq
t = int(input())
tcs = []
for _ in range(t):
    k = int(input())
    tcs.append(list(map(int, input().split())))
def get_cost(files):
    heapq.heapify(files)
    cost = 0
    while len(files) >= 2:
        n1, n2 = heapq.heappop(files), heapq.heappop(files)
        s = n1 + n2
        cost += s
        heapq.heappush(files, s)
    return cost
for tc in tcs:
    print(get_cost(tc))