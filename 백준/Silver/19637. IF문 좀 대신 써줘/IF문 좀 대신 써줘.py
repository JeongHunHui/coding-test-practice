from bisect import bisect_left
n, m = map(int, input().split())
title = []
power = []
for _ in range(n):
    k, v = input().split()
    title.append(k)
    power.append(int(v))
values = [int(input()) for _ in range(m)]
for value in values:
    print(title[bisect_left(power, value)])