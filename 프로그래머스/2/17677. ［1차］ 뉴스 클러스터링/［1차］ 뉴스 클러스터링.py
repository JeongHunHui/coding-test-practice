from collections import Counter
import math

const_num = 65536

def make_set(s):
    s = s.lower()
    return Counter([s[i:i+2] for i in range(len(s)-1) if s[i:i+2].isalpha()])

def solution(str1, str2):
    sets_1 = make_set(str1)
    sets_2 = make_set(str2)
    count_1 = sum((sets_1 & sets_2).values())
    count_2 = sum((sets_1 | sets_2).values())
    return math.floor(count_1 / count_2 * const_num) if count_2 > 0 else const_num