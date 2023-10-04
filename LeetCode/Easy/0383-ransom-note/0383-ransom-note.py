class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in ransomNote:
            if c in dic:
                dic[c] -= 1
                if dic[c] < 0:
                    return False
            else:
                return False
        return True