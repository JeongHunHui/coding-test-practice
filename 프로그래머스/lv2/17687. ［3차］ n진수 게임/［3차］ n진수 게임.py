import string

num_string = string.digits + string.ascii_uppercase

def convert_num(num, base):
    result = ""
    while num > 0:
        result += num_string[num % base]
        num //= base
    return result[::-1] if result != "" else '0'

def solution(n, t, m, p):
    current_num = 0
    current_seq = 1
    answer = ""
    while True:
        converted_num_str = convert_num(current_num, n)
        for c in converted_num_str:
            if current_seq == p:
                answer += c
            current_seq = current_seq % m + 1
            if len(answer) >= t:
                return answer
        current_num += 1
    return -1