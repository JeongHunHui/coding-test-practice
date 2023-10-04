class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while right > left:
            l = s[left]
            if not l.isalpha() and not l.isnumeric():
                left += 1
                continue
            r = s[right]
            if not r.isalpha() and not r.isnumeric():
                right -= 1
                continue
            if l.lower() != r.lower():
                return False
            left += 1
            right -= 1
        return True