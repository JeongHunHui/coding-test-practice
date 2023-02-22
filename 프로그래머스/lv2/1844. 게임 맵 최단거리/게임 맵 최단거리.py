from collections import deque

def solution(maps):
    col_count = len(maps)
    row_count = len(maps[0])
    col = 0
    row = 0
    col_move = [0, 0, 1, -1]
    row_move = [1, -1, 0, 0]
    is_visited = [[0 for _ in range(row_count)] for _ in range(col_count)]
    
    def bfs():
        q = deque()
        q.append(0)
        q.append(0)
        q.append(1)
        
        while len(q) > 0:
            c = q.popleft()
            r = q.popleft()
            d = q.popleft()
            if c == col_count-1 and r == row_count-1:
                return d
            for i in range(len(col_move)):
                new_col = c + col_move[i]
                new_row = r + row_move[i]
                if new_col >= col_count or new_col < 0 or new_row >= row_count or new_row < 0 or maps[new_col][new_row] == 0 or is_visited[new_col][new_row] == 1:
                    continue
                is_visited[new_col][new_row] = 1
                q.append(new_col)
                q.append(new_row)
                q.append(d+1)
        return -1
    
    return bfs()