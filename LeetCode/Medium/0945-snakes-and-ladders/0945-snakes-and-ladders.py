from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_pos(num):
            num -= 1
            val, left = divmod(num, n)
            x = left if val % 2 == 0 else (n-1) - left
            y = (n-1) - val
            return x, y

        visited_num = set()
        visited_num.add(1)
        que = deque([[1,1]])
        while que:
            num, count = que.popleft()
            for i in range(1,7):
                new_num = num + i
                if new_num > n*n:
                    continue
                x, y = get_pos(new_num)
                if board[y][x] != -1:
                    new_num = board[y][x]
                if new_num in visited_num:
                    continue
                if new_num == n*n:
                    return count
                visited_num.add(new_num)
                que.append([new_num, count+1])
        return -1