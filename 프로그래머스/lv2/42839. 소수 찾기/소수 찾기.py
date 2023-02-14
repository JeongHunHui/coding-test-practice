from itertools import permutations

def solution(numbers):
    answer = []
    numbers = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))
    new_nums = [int("".join(p)) for p in per]
    
    for i in new_nums:
        if i < 2:
            continue
        is_prime = True
        for n in range(2, int(i**0.5)+1):
            if i % n == 0:
                is_prime = False
                break
        if is_prime:
            answer.append(i)
    
    return len(set(answer))