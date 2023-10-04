class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        CHECK_COUNT = 2
        point = 0
        count = 1
        for i in range(1,len(nums)):
            num = nums[i]
            if num == nums[i-1]:
                if count < CHECK_COUNT:
                    count += 1
                    point += 1
                    nums[point] = num
            else:
                count = 1
                point += 1
                nums[point] = num
        return point+1