from collections import deque
from math import ceil

def get_left_day(progress, speed):
    return ceil((100 - progress) / speed)

def solution(progresses, speeds):
    left_days = []
    for i in range(len(progresses)):
        progress, speed = progresses[i], speeds[i]
        left_days.append(get_left_day(progress, speed))
        left_day_que = deque(left_days)
        
    max_day = left_days[0]
    complate_task_count = 0
    answer = []
    
    while left_day_que:
        left_day = left_day_que.popleft()
        if max_day < left_day:
            max_day = left_day
            answer.append(complate_task_count)
            complate_task_count = 1
        else:
            complate_task_count += 1
    answer.append(complate_task_count)
    return answer