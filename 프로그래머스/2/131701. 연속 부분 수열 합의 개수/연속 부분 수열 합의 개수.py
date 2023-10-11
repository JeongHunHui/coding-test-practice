def solution(elements):
    nums = []
    elements_len = len(elements)
    elements += elements
    for i in range(1, elements_len):
        for j in range(0, elements_len):
            nums.append(sum(elements[j:j+i]))
    return len(set(nums)) + 1