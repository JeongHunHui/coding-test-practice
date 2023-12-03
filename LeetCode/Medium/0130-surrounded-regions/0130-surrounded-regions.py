from collections import deque
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        x_len = len(board[0])
        y_len = len(board)

        def bfs(x, y, board):
            que = deque()
            que.append([x,y])
            board[y][x] = 'X'
            visited_regions = [[x,y]]
            is_surrounded = True
            while que:
                x, y = que.popleft()
                for dx, dy in dirs:
                    nx, ny = dx+x, dy+y
                    if nx < 0 or nx >= x_len or ny < 0 or ny >= y_len:
                        is_surrounded = False
                        continue
                    if board[ny][nx] == 'X':
                        continue
                    board[ny][nx] = 'X'
                    que.append([nx,ny])
                    visited_regions.append([nx,ny])
            return is_surrounded, visited_regions
        
        for y in range(1,y_len-1):
            for x in range(1,x_len-1):
                if board[y][x] != 'O':
                    continue
                is_surrounded, visited_regions = bfs(x, y, copy.deepcopy(board))
                c = 'X' if is_surrounded else '-'
                for nx, ny in visited_regions:
                    board[ny][nx] = c
        
        for y in range(y_len):
            for x in range(x_len):
                if board[y][x] == '-':
                    board[y][x] = 'O'