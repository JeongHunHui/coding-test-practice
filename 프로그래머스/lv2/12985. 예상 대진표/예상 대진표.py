import math

def solution(n,a,b):
    match_count = math.log(n, 2)
    while match_count > 1:
        n /= 2
        if (a > n and b <= n) or (a <= n and b > n):
            return match_count
        if a - n > 0:
            a -= n
            b -= n
        match_count -= 1
    return match_count