def solution(n):
    before = 1
    answer = 1
    for i in range(2, n+1):
        temp = (before + answer) % 1000000007
        before = answer
        answer = temp
    return answer