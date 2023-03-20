import string

num_string = string.digits + string.ascii_uppercase

def convert_num(num, base):
    s, r = divmod(num, base)
    if s == 0: return num_string[r]
    return convert_num(s, base) + num_string[r]

def solution(n, t, m, p):
    answer = ''
    count = 0
    turn = 0
    is_not_finish = True
    while is_not_finish:
        word = convert_num(turn, n)
        for c in word:
            if count % m + 1 == p:
                answer += c
                if len(answer) == t:
                    is_not_finish = False
                    break
            count += 1
        turn += 1
    return answer