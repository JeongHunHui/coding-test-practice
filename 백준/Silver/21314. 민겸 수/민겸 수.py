# 11:00
# 가장 작은 값과 가장 큰 값
# 가장 작은 값: k앞에서 끊기
# 가장 큰 값: k가 나오면 바로 끊기
m_num = input()
min_num = ''
max_num = ''
temp = 0
for c in m_num:
    if c == 'M':
        temp += 1
    else:
        if temp != 0:
            min_num += '1' + '0'*(temp-1)
        min_num += '5'
        max_num += '5' + '0'*temp
        temp = 0
max_num += '1'*temp
if temp != 0:
    min_num += '1' + '0'*(temp-1)
print(max_num)
print(min_num)