class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits = [c for c in digits]
        l = len(digits)
        digit_dict ={
            '2':['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        answer = []
        def backtracking(word, depth):
            if depth == l:
                answer.append(word)
                return
            for c in digit_dict[digits[depth]]:
                backtracking(word+c, depth+1)
        backtracking('',0)
        return answer