from collections import deque
import math

def convert_num_str(n, k):
    digits = deque()
    while n > 0:
        digits.appendleft(str(n%k))
        n //= k
    return ''.join(digits)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    converted_num_str = convert_num_str(n,k)
    target_nums = converted_num_str.split('0')
    return len([1 for x in target_nums if x != '' and is_prime(int(x))])