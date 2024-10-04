# 23:46
from collections import deque

w, h = map(int, input().split())
grid = []
costs = [[[float('inf')] * 4 for _ in range(w)] for _ in range(h)]
temp = []
for y in range(h):
    row = []
    x = 0
    for c in input():
        if c == 'C': temp.append((x, y))
        row.append(c)
        x += 1
    grid.append(row)


directions = [(0,1),(0,-1),(1,0),(-1,0)]
start, end = temp
sx, sy = start
ex, ey = end
answer = float('inf')
dq = deque([(sx, sy, i, 0) for i in range(4)])

while dq:
    x, y, direction, mirror_count = dq.popleft()
    if ex == x and ey == y:
        answer = min(mirror_count, answer)
        continue
    for i in range(4):
        nx, ny = x+directions[i][0], y+directions[i][1]
        if nx >= w or nx < 0 or ny >= h or ny < 0:
            continue
        temp_mirror_count = mirror_count if i == direction else mirror_count + 1
        if grid[ny][nx] == '*' or costs[ny][nx][i] <= temp_mirror_count:
            continue
        dq.append((nx, ny, i, temp_mirror_count))
        costs[ny][nx][i] = temp_mirror_count
print(answer)