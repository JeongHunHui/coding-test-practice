from itertools import combinations

def solution(numbers, target):
    answer = 0
    num_sum = sum(numbers)
    for i in range(len(numbers)):
        new_nums = combinations(numbers, i+1)
        for nums in new_nums:
            num = num_sum + sum([-2 * n for n in nums])
            if target == num:
                answer += 1
    return answer