import string, math

datas = string.digits+string.ascii_lowercase

def convert_int(num, base):
    s, r = divmod(num, base)
    return datas[r] if s == 0 else str(convert_int(s, base)) + datas[r]

def is_prime(num):
    if num == 1: return False
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num % i == 0:return False
    return True
    
def solution(n, k):
    return len([1 for c in convert_int(n,k).split('0') if c != '' and is_prime(int(c))])
