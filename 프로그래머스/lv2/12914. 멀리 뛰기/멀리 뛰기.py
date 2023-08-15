from math import comb

def solution(n):
    answer = 1
    max_two_count = n // 2
    min_one_count = n % 2
    while max_two_count > 0:
        answer += comb(max_two_count + min_one_count, min_one_count)
        max_two_count -= 1
        min_one_count += 2
    return answer % 1234567