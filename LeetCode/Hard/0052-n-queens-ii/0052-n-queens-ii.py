class Solution:
    def totalNQueens(self, n: int) -> int:
        # x
        visited_x = set()
        # \
        visited_diagonal = set()
        # /
        visited_antidiagonal = set()

        answer = 0

        def backtracking(y):
            nonlocal answer
            if y == n:
                answer += 1
                return
            for x in range(n):
                if x not in visited_x and x+y not in visited_diagonal and x-y not in visited_antidiagonal:
                    visited_x.add(x)
                    visited_diagonal.add(x+y)
                    visited_antidiagonal.add(x-y)
                    backtracking(y+1)
                    visited_x.remove(x)
                    visited_diagonal.remove(x+y)
                    visited_antidiagonal.remove(x-y)
        
        backtracking(0)
        return answer