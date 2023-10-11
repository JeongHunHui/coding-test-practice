from collections import deque

def solution(priorities, location):
    process_queue = deque(enumerate(priorities))
    
    def get_max_priority():
        return max(process_queue, key = lambda x: x[1])[1]
    
    max_priority = get_max_priority()
    count = 0
    
    while process_queue:
        current_process = process_queue.popleft()
        current_location, current_priorties = current_process
        if max_priority == current_priorties:
            count += 1
            if location == current_location:
                return count
            max_priority = get_max_priority()
        else:
            process_queue.append(current_process)
    
    return -1