from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def opterate(n1, n2, opterator):
            if opterator == '+':
                return n1 + n2
            elif opterator == '-':
                return n1 - n2
            elif opterator == '*':
                return n1 * n2
            elif opterator == '/':
                return int(n1 / n2)
        numQue = deque()
        operatorQue = deque()
        for token in tokens:
            try:
                numQue.append(int(token))
            except ValueError:
                operatorQue.append(token)
                if len(numQue) > 1:
                    n1 = numQue.pop()
                    n2 = numQue.pop()
                    opterator = operatorQue.pop()
                    numQue.append(opterate(n2, n1, opterator))
        return numQue.pop()