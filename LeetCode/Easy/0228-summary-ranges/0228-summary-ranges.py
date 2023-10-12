class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        answer, temp, p, l = [], nums[0], 0, len(nums)
        for i in range(1, len(nums)):
            num = nums[i]
            if num != temp+1:
                n = nums[p]
                answer.append(str(n) if i - p == 1 else f'{n}->{temp}')
                p = i
            temp = num
        n = nums[p]
        return answer + [str(n) if l - p == 1 else f'{n}->{temp}']