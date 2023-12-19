class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane_algorithm(nums):
            dp = [nums[0]]
            answer = dp[0]
            for i in range(1, len(nums)):
                num = nums[i]
                val = max(dp[i-1]+num, num)
                answer = max(answer, val)
                dp.append(val)
            return answer
        # case1 - 일반적인 경우
        answer1 = kadane_algorithm(nums)
        # case2 - 원형 배열의 경우
        # -> 배열의 합을 구하고, 배열을 반전 시켜 최소합을 구해서 더하기
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = -nums[i]
        answer2 = total + kadane_algorithm(nums)
        if answer2 == 0:
            return answer1
        return max(answer1, answer2)