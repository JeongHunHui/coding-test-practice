def gcd(a,b):
    if b > a:
        i = a
        a = b
        b = i
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = i * answer // gcd(answer, i)
    return answer