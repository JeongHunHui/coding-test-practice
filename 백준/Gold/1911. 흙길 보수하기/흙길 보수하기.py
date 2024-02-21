# 03:23
import math
n, l = map(int, input().split())
pools = []
for _ in range(n):
    start, end = map(int, input().split())
    pools.append((start, end))
pools.sort(key=lambda x: x[0])
check_point = -1
answer = 0
for start, end in pools:
    if check_point >= end-1:
        continue
    if start <= check_point:
        start = check_point+1
    pool_count = end-start
    wood_count = math.ceil(float(pool_count)/float(l))
    answer += wood_count
    check_point = start + l * wood_count - 1
print(answer)