# 13:37
from collections import Counter, deque
counter = Counter()
answer = 0
que = deque()

n, k = map(int, input().split())
nums = list(map(int, input().split()))
for num in nums:
    counter.update([num])
    if counter[num] > k:
        while counter[num] > k:
            temp_num = que.popleft()
            counter[temp_num] -= 1
    que.append(num)
    answer = max(answer, len(que))
print(answer)