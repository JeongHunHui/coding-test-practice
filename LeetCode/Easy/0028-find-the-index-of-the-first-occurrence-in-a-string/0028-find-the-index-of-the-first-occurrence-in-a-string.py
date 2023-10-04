class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_l = len(needle)
        i = 0
        while i < len(haystack):
            print(haystack[i:i+n_l])
            if needle == haystack[i:i+n_l]:
                return i
            i += 1
        return -1