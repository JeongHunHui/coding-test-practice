class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda e: e[0])
        start, end = points[0]
        answer = 1
        for s, e in points[1:]:
            if end < s:
                answer += 1
                start, end = s, e
            else:
                start = max(s,start)
                end = min(e,end)
        return answer

            