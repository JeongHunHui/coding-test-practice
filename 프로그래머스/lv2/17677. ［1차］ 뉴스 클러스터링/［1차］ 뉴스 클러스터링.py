from collections import Counter
import math

const_num = 65536

def make_set(s):
    s = s.lower()
    s_counter = Counter([s[i:i+2] for i in range(len(s)-1)])
    s_counter = Counter({k: v for k, v in s_counter.items() if k.isalpha()})
    return s_counter

def solution(str1, str2):
    sets_1 = make_set(str1)
    sets_2 = make_set(str2)
    count_1 = sum((sets_1 & sets_2).values())
    count_2 = sum((sets_1 | sets_2).values())
    if count_2 == 0:
        return const_num
    return math.floor(count_1 / count_2 * const_num)