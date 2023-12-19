class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = 0~i까지 최대 값
        dp = [nums[0]]
        answer = dp[0]
        for i in range(1, len(nums)):
            num = nums[i]
            val = max(dp[i-1]+num, num)
            dp.append(val)
            answer = max(val, answer)
        return answer