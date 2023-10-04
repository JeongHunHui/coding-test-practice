class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer, start, checkDict = 0, 0, {}
        for i, c in enumerate(s):
            if c in checkDict and checkDict[c] >= start:
                answer = max(answer, i-start)
                start = checkDict[c]+1
            checkDict[c] = i
        return max(answer, len(s)-start)