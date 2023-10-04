from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordDict = {}
        wordSet = set()
        count = 1
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 not in wordDict:
                if c2 in wordSet:
                    return False
                wordDict[c1] = c2
                wordSet.add(c2)
            elif wordDict[c1] != c2:
                return False
        return True