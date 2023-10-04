class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                answer += 1
            elif answer != 0:
                return answer
        return answer