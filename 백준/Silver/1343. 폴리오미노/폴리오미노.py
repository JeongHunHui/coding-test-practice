# 23:44
temp = ''
answer = ''
for c in input():
    if c == '.':
        if temp != '':
            l = len(temp)
            if l % 2 == 1:
                answer = '-1'
                break
            a_count = l // 4
            b_count = 0 if l % 4 == 0 else 1
            answer += 'AAAA'*a_count + 'BB'*b_count
            temp = ''
        answer += '.'
    else:
        temp += c

if temp != '':
    l = len(temp)
    if l % 2 == 1:
        answer = '-1'
    else:
        a_count = l // 4
        b_count = 0 if l % 4 == 0 else 1
        answer += 'AAAA'*a_count + 'BB'*b_count
        temp = ''

print(answer)