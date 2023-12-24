# 13:20
from collections import deque
import math
n, k = map(int, input().split())
if n >= k:
  print(n-k)
else:
  # dp[i] = i번째 칸에 도달할 수 있는 최소 시간
  # dp[i] = min(dp[i+1],dp[i-1],dp[i/2])+1
  dp = [math.inf] * (1+max(n,k)*2)
  dp[n] = 0
  que =  deque([(n, 0)])
  while que:
    num, depth = que.popleft()
    forward = num+1
    if forward < len(dp) and dp[forward] > depth + 1:
      dp[forward] = depth + 1
      que.append((forward, depth+1))
    back = num-1
    if back >= 0 and dp[back] > depth + 1:
      dp[back] = depth + 1
      que.append((back, depth+1))
    double = num*2
    if double < len(dp) and dp[double] > depth + 1:
      dp[double] = depth + 1
      que.append((double, depth+1))
    if forward == k or double == k or back == k:
      print(dp[k])
      break