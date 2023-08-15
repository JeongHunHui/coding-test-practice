from math import gcd

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = i * answer // gcd(answer, i)
    return answer