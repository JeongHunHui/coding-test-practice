from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        cDict = {')':'(',']':'[','}':'{'}
        cQue = deque(s[0])
        for c in s[1:]:
            if c in cDict and cQue and cDict[c] == cQue[-1]:
                cQue.pop()
            else:
                cQue.append(c)
        return not cQue