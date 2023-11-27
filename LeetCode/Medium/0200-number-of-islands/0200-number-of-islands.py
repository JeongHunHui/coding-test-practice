from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        x_len = len(grid[0])
        y_len = len(grid)
        def bfs(x,y):
            que = deque()
            que.append((x,y))
            grid[y][x] = "2"
            while que:
                x, y = que.pop()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if nx >= 0 and nx < x_len and ny >= 0 and ny < y_len and grid[ny][nx] == "1":
                        que.append((nx,ny))
                        grid[ny][nx] = "2"
        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == "1":
                    answer += 1
                    bfs(x,y)
        return answer