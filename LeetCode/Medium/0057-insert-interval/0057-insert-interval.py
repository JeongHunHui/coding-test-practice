class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        midS, midE = start, end
        leftList, rightList = [], []
        for s, e in intervals:
            # left
            if start > e:
                leftList.append([s,e])
            # right
            elif s > end:
                rightList.append([s,e])
            # mid
            else:
                midS = min(s,midS)
                midE = max(e,midE)
        return leftList + [[midS, midE]] + rightList