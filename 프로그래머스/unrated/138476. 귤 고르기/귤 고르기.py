from collections import Counter

def solution(k, tangerine):
    tangerine_counter = Counter(tangerine)
    deletable_count = len(tangerine) - k
    type_count = len(tangerine_counter)
    sorted_tangerine = sorted(tangerine_counter.items(), key=lambda x: x[1])
    for tang in sorted_tangerine:
        deletable_count -= tang[1]
        if deletable_count < 0:
            return type_count
        type_count -= 1
    return type_count