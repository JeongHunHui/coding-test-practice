class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pre_val = nums[0]
        for i in range(1, len(nums)):
            pre_val -= 1
            if pre_val < 0:
                return False
            current_val = nums[i]
            pre_val = max(pre_val, current_val)
        return True