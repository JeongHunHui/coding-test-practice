class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                # 피크는 오른쪽에 있을 수 있음
                left = mid + 1
            else:
                # 피크는 왼쪽에 있을 수 있음
                right = mid
        return left