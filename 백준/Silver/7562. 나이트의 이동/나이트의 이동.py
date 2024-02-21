# 03:06
from collections import deque
dirs = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
t = int(input())
tc_list = []
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    nx, ny = map(int, input().split())
    tc_list.append((l, (sx,sy), (nx,ny)))
for l, s_pos, k_pos in tc_list:
    sx, sy = s_pos
    kx, ky = k_pos
    que = deque([(sx, sy, 0)])
    is_visited = [[False]*l for _ in range(l)]
    is_visited[sy][sx] = True
    while que:
        x, y, count = que.popleft()
        if x == kx and y == ky:
            print(count)
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < l and ny >= 0 and ny < l and not is_visited[ny][nx]:
                is_visited[ny][nx] = True
                que.append((nx, ny, count+1))