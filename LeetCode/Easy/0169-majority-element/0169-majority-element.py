class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_dict = defaultdict(int)
        majority_count = math.ceil(len(nums)/2)
        for num in nums:
            element_dict[num] += 1
        for key, value in element_dict.items():
            if value >= majority_count:
                return key
        return -1
