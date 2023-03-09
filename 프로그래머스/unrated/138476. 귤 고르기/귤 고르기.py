def solution(k, tangerine):
    # count_arr = [tangerine.count(i) for i in set(tangerine)]
    # count_arr.sort(reverse = True)
    answer = 0
    count_dict = {}
    for i in tangerine:
        if i in count_dict: count_dict[i] += 1
        else: count_dict[i] = 1
    count_arr = list(count_dict.values())
    count_arr.sort(reverse = True)
    for count in count_arr:
        answer += 1
        k -= count
        if k <= 0: break
    return answer