class Solution:
    def totalNQueens(self, n: int) -> int:
        # 방문한 x
        v_x = set()
        # 대각선 \ -> x-y가 같으면 같은 대각선
        v_diagonal = set()
        # 반 대각선 / -> x+y가 같으면 같은 반대각선
        v_antidiagonal = set()
        
        answer = 0
        def backtracking(y):
            nonlocal answer
            if y == n:
                answer += 1
                return
            for x in range(n):
                if x not in v_x and x-y not in v_diagonal and x+y not in v_antidiagonal:
                    v_x.add(x)
                    v_diagonal.add(x-y)
                    v_antidiagonal.add(x+y)
                    backtracking(y+1)
                    v_x.remove(x)
                    v_diagonal.remove(x-y)
                    v_antidiagonal.remove(x+y)
        
        backtracking(0)
        return answer