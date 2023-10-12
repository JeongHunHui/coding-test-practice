class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet, checkSet, maxLen = set(nums), set(), 0
        for num in numSet:
            if num in checkSet:
                continue
            n, l = num+1, 1
            while n in numSet:
                checkSet.add(n)
                l += 1
                n += 1
            n =  num-1
            while n in numSet:
                checkSet.add(n)
                l += 1
                n -= 1
            maxLen = max(l,maxLen)
        return maxLen