def solution(n):
    pre_num = 0
    current_num = 1
    for i in range(3, n+1):
        answer = pre_num + current_num
        pre_num = current_num
        current_num = answer
    return (pre_num + current_num)%1234567