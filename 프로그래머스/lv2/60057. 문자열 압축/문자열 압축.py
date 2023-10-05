def compression(s, n):
    answer = ''
    count = 0
    cStr = s[0:n]
    temp = ''
    for i in range(0,len(s),n):
        temp = s[i:i+n]
        if cStr == temp:
            count += 1
        else:
            answer += f'{count if count != 1 else ""}{cStr}'
            cStr = temp
            count = 1
    return len(answer + f'{count if count != 1 else ""}{cStr}')

def solution(s):
    l = len(s)
    answer = l
    for n in range(1,l):
        answer = min(answer, compression(s, n))
    return answer