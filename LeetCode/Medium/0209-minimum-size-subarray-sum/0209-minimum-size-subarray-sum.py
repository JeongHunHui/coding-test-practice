class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        start, size, total, answer = 0, 1, nums[0], float('inf')
        if total >= target:
            return 1
        while start + size <= l and answer != 1:
            if total < target:
                if start + size >= l:
                    break
                total += nums[start+size]
                size += 1
            elif size == 1:
                start += 1
                total = nums[start]
            else:
                total -= nums[start]
                start += 1
                size -= 1
            if total >= target:
                answer = min(answer, size)
        return answer if answer != float('inf') else 0