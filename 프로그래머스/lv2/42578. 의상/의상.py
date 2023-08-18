from functools import reduce

def solution(clothes):
    cloth_dict = {}
    for cloth_name, cloth_type in clothes:
        if cloth_type in cloth_dict:
            cloth_dict[cloth_type] += 1
        else:
            cloth_dict[cloth_type] = 2
    return reduce(lambda x, y: x * y, cloth_dict.values()) - 1