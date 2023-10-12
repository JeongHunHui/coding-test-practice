class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        while n not in numSet:
            numSet.add(n)
            n = sum(int(c)*int(c) for c in str(n))
            if n == 1:
                return True
        return False