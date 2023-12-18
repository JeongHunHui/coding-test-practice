class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_len = len(board[0])
        y_len = len(board)
        word_len = len(word)
        is_visited = [[False]*x_len for _ in range(y_len)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        answer = False
        def backtracking(x,y,depth):
            nonlocal answer
            if depth == word_len:
                answer = True
                return
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < x_len and ny >= 0 and ny < y_len and not is_visited[ny][nx] and word[depth] == board[ny][nx]:
                    is_visited[ny][nx] = True
                    backtracking(nx, ny, depth+1)
                    is_visited[ny][nx] = False
        
        for y in range(y_len):
            for x in range(x_len):
                if word[0] != board[y][x]:
                    continue
                is_visited[y][x] = True
                backtracking(x,y,1)
                is_visited[y][x] = False
                if answer:
                    break
            if answer:
                break
        return answer
