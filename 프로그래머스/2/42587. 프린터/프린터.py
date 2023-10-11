from collections import deque
def solution(priorities, location):
    answer = 0
    datas = [[i, priorities[i]] for i in range(len(priorities))]
    q = deque(datas)
    while q:
        data = q.popleft()
        is_go_back = False
        for arr in q:
            if arr[1] > data[1]:
                q.append(data)
                is_go_back = True
                break
        if not is_go_back:
            answer += 1
            if location == data[0]:
                break
    return answer