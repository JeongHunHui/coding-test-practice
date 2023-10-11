from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people_deque = deque(people)
    while len(people_deque) > 0:
        answer += 1
        max_kg = people_deque.pop()
        if len(people_deque) == 0:
            break
        min_kg = people_deque.popleft()
        if max_kg + min_kg > limit:
            people_deque.appendleft(min_kg)
    return answer