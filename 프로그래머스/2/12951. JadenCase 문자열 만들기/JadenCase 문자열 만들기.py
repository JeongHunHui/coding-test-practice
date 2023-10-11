def solution(s):
    answer = ''
    buffer = ''
    for c in s:
        if c == ' ':
            buffer += c
            answer += buffer
            buffer = ''
        else:
            if buffer == '':
                buffer += c.upper()
            else:
                buffer += c.lower()
    answer += buffer
    return answer