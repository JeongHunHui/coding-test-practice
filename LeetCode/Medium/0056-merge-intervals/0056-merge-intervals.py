class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])
        answer = []
        s, e = intervals[0]
        for start, end in intervals[1:]:
            if start <= e:
                e = max(e,end)
            else:
                answer.append([s,e])
                s = start
                e = end
        return answer + [[s,e]]