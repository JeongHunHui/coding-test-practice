class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = set()
        for i in range(len(nums)-2):
            n1 = nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                n2, n3 = nums[j], nums[k]
                s = n1+n2+n3
                if s == 0:
                    sums.add(f'{n1},{n2},{n3}')
                if s > 0:
                    k -= 1
                else:
                    j += 1
        return [list(map(int,s.split(','))) for s in sums]