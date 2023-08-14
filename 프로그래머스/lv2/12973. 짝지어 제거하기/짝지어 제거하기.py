def solution(s):
    answer = []
    buffer = ''
    for i in range(0, len(s)):
        c = s[i]
        if c != buffer:
            if buffer != '':
                answer.append(buffer)
            buffer = c
        else:
            if len(answer) > 0:
                buffer = answer.pop()
            else:
                buffer = ''
    if buffer == '':
        return 1
    else:
        return 0