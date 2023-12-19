class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums += row
        low, high = 0, len(nums)
        while low < high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return 0 <= low < len(nums) and nums[low] == target