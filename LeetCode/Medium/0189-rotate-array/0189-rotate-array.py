class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) - k % len(nums)
        nums[:] = nums[n:] + nums[:n]
        