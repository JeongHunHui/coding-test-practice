# 02:58
# n = 코스 수
# k = 이동 거리
n, k = map(int, input().split())
course = list(map(int, input().split()))

def solve():
    total = 0
    for i, c in enumerate(course):
        total += c
        if total > k:
            return i
    
    for i in range(n-1, -1, -1):
        c = course[i]
        total += c
        if total > k:
            return i
    return 0

print(solve()+1)