from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while len(scoville) > 1:
        first_value = heappop(scoville)
        if first_value >= K:
            return answer
        second_value = heappop(scoville)
        heappush(scoville, first_value + second_value * 2)
        answer += 1
    return answer if heappop(scoville) >= K else -1