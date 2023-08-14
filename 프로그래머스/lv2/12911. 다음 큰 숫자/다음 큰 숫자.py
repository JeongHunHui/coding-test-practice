def get_bin_one_count(n):
    return len(bin(n)[2:].replace('0',''))

def solution(n):
    answer = n
    count = get_bin_one_count(n)
    while True:
        answer += 1
        if count == get_bin_one_count(answer):
            return answer