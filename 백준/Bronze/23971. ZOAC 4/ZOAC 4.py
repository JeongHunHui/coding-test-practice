# 11:05
import math
i, j, n, m = map(int, input().split())
print(math.ceil(i/(n+1)) * math.ceil(j/(m+1)))