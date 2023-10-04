class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        answer, first_s, last_s = '', strs[0], strs[-1]
        for i in range(min(len(first_s), len(last_s))):
            c = first_s[i]
            if c == last_s[i]:
                answer += c
            else:
                return answer
        return answer