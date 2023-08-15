def solution(k, tangerine):
    tangerine_dict = {}
    deletable_count = len(tangerine) - k
    for i in tangerine:
        if i in tangerine_dict:
            tangerine_dict[i] += 1
        else:
            tangerine_dict[i] = 1
    type_count = len(tangerine_dict)
    sorted_tangerine = sorted(tangerine_dict.items(), key=lambda x: x[1])
    sorted_tangerine_dict = dict(sorted_tangerine)
    for key in sorted_tangerine_dict:
        deletable_count -= sorted_tangerine_dict[key]
        if deletable_count < 0:
            return type_count
        type_count -= 1
    return type_count