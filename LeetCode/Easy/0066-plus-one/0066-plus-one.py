class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(c) for c in str(int(''.join(map(str, digits))) + 1)]