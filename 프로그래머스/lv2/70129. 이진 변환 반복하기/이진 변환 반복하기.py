def to_bin(s):
    pre_len = len(s)
    s = s.replace("0", "")
    new_len = len(s)
    remove_zero_count = pre_len - new_len
    return new_len, remove_zero_count

def solution(s):
    count = 0
    remove_zero = 0
    new_s = s
    while new_s != "1":
        new_len, remove_zero_count = to_bin(new_s)
        new_s = bin(new_len)[2:]
        remove_zero += remove_zero_count
        count += 1
    return [count, remove_zero]