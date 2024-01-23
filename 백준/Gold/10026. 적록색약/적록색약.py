# 13:16
from collections import deque
n = int(input())
grid = [[c for c in input()] for _ in range(n)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False]*n for _ in range(n)]
blind_visited = [[False]*n for _ in range(n)]

def bfs(x,y,is_blind):
    que = deque([(x,y)])
    c = grid[y][x]
    c_set = set([c])
    if is_blind:
        if c == 'R':
            c_set.add('G')
        elif c == 'G':
            c_set.add('R')
    visited[y][x] = True
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < n and grid[ny][nx] in c_set:
                if not is_blind and not visited[ny][nx]:
                    que.append((nx, ny))
                    visited[ny][nx] = True
                elif is_blind and not blind_visited[ny][nx]:
                    que.append((nx, ny))
                    blind_visited[ny][nx] = True

answer1 = 0
answer2 = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(x,y,False)
            answer1 += 1
        if not blind_visited[y][x]:
            bfs(x,y,True)
            answer2 += 1

print(f'{answer1} {answer2}')