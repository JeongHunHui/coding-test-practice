# 11:34
from collections import defaultdict
n, c = map(int, input().split())
nums = list(map(int, input().split()))
num_dict = defaultdict(int)
for num in nums:
    num_dict[num] += 1
answer = []
for num, count in sorted(list(num_dict.items()), key = lambda x: x[1], reverse = True):
    for _ in range(count):
        answer.append(str(num))
print(' '.join(answer))