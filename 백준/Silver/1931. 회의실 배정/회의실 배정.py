# 57
n = int(input())
record = [list(map(int, input().split())) for _ in range(n)]
record.sort(key = lambda x: (x[0], x[1]), reverse = True)
num = record.pop()[1]
count = 1
while record:
    s, f = record.pop()
    if num <= s:
        count += 1
        num = f
        continue
    if f < num:
        num = f
print(count)