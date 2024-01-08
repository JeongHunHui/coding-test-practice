# 15:10
n, m = map(int, input().split())
records = list(map(int, input().split()))
start, end = max(records), sum(records)

while start < end:
    mid = (start + end)//2
    count = 1
    time_sum = 0
    for record in records:
        temp = time_sum + record
        if temp > mid:
            count += 1
            time_sum = record
        else:
            time_sum = temp
    if count <= m:
        end = mid
    elif count > m:
        start = mid + 1

print(start)