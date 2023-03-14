import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        min_scoville = heapq.heappop(scoville)
        if min_scoville >= K: break
        second_scoville = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scoville + second_scoville * 2)
        answer += 1
    return answer if heapq.heappop(scoville) >= K else -1