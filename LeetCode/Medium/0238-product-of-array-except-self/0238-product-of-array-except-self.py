class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        c_num = nums[0]
        for i in range(1,len(nums)):
            answer[i] = c_num
            c_num *= nums[i]
        c_num = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            answer[i] *= c_num
            c_num *= nums[i]
        return answer