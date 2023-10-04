class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer, left, right = 0, 0, len(height)-1
        while left < right:
            h1, h2 = height[left], height[right]
            answer = max(answer, min(h1, h2) * (right-left))
            if h2 > h1:
                left += 1
            else:
                right -= 1
        return answer