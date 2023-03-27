from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    left_truck = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    current_weight = 0
    while not(len(left_truck) == 0 and current_weight == 0):
        current_weight -= bridge.popleft()
        answer += 1
        if len(left_truck) == 0 or current_weight + left_truck[0] > weight:
            bridge.append(0)
        else:
            start_truck = left_truck.popleft()
            bridge.append(start_truck)
            current_weight += start_truck
    return answer