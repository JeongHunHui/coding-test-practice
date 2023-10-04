class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num != nums[i-1]:
                nums[count] = num
                count += 1
        return count