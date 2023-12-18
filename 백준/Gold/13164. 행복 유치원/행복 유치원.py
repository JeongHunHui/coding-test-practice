# 23:03
# n명을 k조로 만드는데, 키 차이가 덜 나야됨
n, k = map(int, input().split())
heights = list(map(int, input().split()))
diffs = sorted([heights[i] - heights[i-1] for i in range(1, n)], reverse=True)
print(sum(diffs[k-1:]))