def solution(s):
    answer = ['', s[0]]
    for c in s[1:]:
        answer.pop() if c == answer[-1] else answer.append(c)
    return 0 if len(answer) > 1 else 1