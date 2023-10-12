class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, n in enumerate(nums):
            if target - n in numDict:
                return [numDict[target-n],i]
            numDict[n] = i