class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()
        if len(set(pattern)) != len(set(s)):
            return False
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = s[i]
            elif dic[pattern[i]] == s[i]:
                continue
            else:
                return False
        return True


        

        