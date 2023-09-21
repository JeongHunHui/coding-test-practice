from collections import Counter
from itertools import combinations

MIN_COUNT = 2

def solution(orders, course):
    answer = []
    for num in course:
        result_list = []
        for order in orders:
            if len(order) >= num:
                result_list += (''.join(sorted(list(s))) for s in list(combinations(order, num)))
        if len(result_list) == 0:
            continue
        order_counter = Counter(result_list)
        max_count = max(MIN_COUNT, Counter(result_list).most_common(1)[0][1])
        filtered_order_counter = Counter({k: v for k, v in order_counter.items() if v == max_count})
        answer += list(filtered_order_counter.keys())
                
    return sorted(answer)