class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
        temp = s[0]
        for c in t:
            if c == temp:
                i += 1
                if i == len(s):
                    return True
                temp = s[i]
        return False