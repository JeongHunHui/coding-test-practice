from collections import deque

pair_dict = {')': '(', ']': '[', '}': '{'}

def is_correct(s):
    new_que = deque([''])
    for c in s:
        if c in pair_dict:
            if pair_dict[c] != new_que.pop():
                return False
        else:
            new_que.append(c)
    return len(new_que) == 1
    
def solution(s):
    answer = 0
    que = deque(s)
    for i in range(len(que)):
        if is_correct(que):
            answer += 1
        que.appendleft(que.pop())
    return answer