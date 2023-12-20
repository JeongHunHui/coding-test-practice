class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        left_num = nums[left]
        # target이 정렬 기준점의 왼쪽에 있으면 True
        near_left = left_num <= target

        while left < right:
            mid = (left+right)//2
            mid_num = nums[mid]
            if mid_num == target:
                left = mid
                break
            # 정렬 기준점의 오른쪽에 있을 때
            if mid_num < left_num:
                if not near_left and mid_num < target:
                    left = mid+1
                else:
                    right = mid
            # 정렬 기준점의 왼쪽에 있을 때
            else:
                if near_left and mid_num > target:
                    right = mid
                else:
                    left = mid+1
        return left if 0<=left<len(nums) and nums[left]==target else -1