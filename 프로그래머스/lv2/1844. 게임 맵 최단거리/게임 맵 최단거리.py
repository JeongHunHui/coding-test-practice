from collections import deque

def solution(maps):
    col = len(maps)
    row = len(maps[0])
    is_visited = [[0 for _ in range(0,row)] for _ in range(0,col)]
    is_visited[0][0] = 1
    
    def bfs():
        q = deque()
        q.append(0)
        q.append(0)
        q.append(1)
        dc = [0,0,1,-1]
        dr = [1,-1,0,0]
        while len(q) > 0:
            c = q.popleft()
            r = q.popleft()
            depth = q.popleft()
            if c == col-1 and r == row-1:
                return depth
            for i in range(0,4):
                new_c = c+dc[i]
                new_r = r+dr[i]
                if new_c < 0 or new_c >= col or new_r < 0 or new_r >= row or is_visited[new_c][new_r] == 1 or maps[new_c][new_r] == 0:
                    continue
                q.append(new_c)
                q.append(new_r)
                q.append(depth+1)
                is_visited[new_c][new_r] = 1
        return -1
    
    return bfs()