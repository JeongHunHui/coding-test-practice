class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = '(', ')'
        answer = []
        def backtracking(current, count, depth):
            if count < 0 or n*2 - depth < count:
                return
            if depth == n * 2:
                answer.append(current)
                return
            backtracking(current+left, count+1, depth+1)
            backtracking(current+right, count-1, depth+1)
        backtracking('',0,0)
        return answer