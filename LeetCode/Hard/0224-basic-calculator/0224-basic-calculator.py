from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        def normalCalculate(que):
            num = 0
            isPlus = True
            while que:
                token = que.popleft()
                try:
                    i = int(token)
                    num += (i if isPlus else -1 * i)
                except ValueError:
                    isPlus = token == '+'
            return num
        tokenQue = deque()
        s += ' '
        temp = ''
        for c in s:
            if c.isnumeric():
                temp += c
                continue
            if temp != '':
                tokenQue.append(temp)
                temp = ''
            if c == ' ':
                continue
            if c != ')':
                tokenQue.append(c)
                continue
            tempQue = deque()
            while True:
                token = tokenQue.pop()
                if token == '(':
                    break
                tempQue.appendleft(token)
            tokenQue.append(str(normalCalculate(tempQue)))
        return normalCalculate(tokenQue)