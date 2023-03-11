def solution(clothes):
    answer = 1
    cloth_dict = {}
    for cloth_arr in clothes:
        category = cloth_arr[1]
        if category in cloth_dict:
            cloth_dict[category] += 1
        else:
            cloth_dict[category] = 2
    for category in cloth_dict:
        answer *= cloth_dict[category]
    return answer - 1