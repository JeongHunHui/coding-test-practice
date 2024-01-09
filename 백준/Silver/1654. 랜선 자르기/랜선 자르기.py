# 16:03
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
start, end = 1, max(lines)
while start <= end:
    mid = (start+end)//2
    count = 0
    for line in lines:
        count += line // mid
    if count < n:
        end = mid - 1
    else:
        start = mid + 1
print(start-1)