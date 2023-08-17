from collections import deque, Counter

member_day = 10 # 회원 지속 기간

def is_want_items(items, want_dict):
    items_counter = dict(Counter(items))
    return want_dict == items_counter

def solution(want, number, discount):
    want_dict = {}
    answer = 0
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    items = deque(discount[:member_day-1])
    
    for i in range(len(discount)-member_day+1):
        items.append(discount[i+member_day-1])
        if is_want_items(items, want_dict):
            answer += 1
        items.popleft()
    return answer