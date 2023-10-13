class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        if l == 0:
            return [newInterval]
        status = 'left' # left, mid, right
        start, end = newInterval
        answer, tempS, tempE = [], l, 0
        for s, e in intervals:
            if s > end:
                if status == 'left':
                    answer.append(newInterval)
                elif status == 'mid':
                    answer.append([tempS, tempE])
                status = 'right'
            elif e >= start:
                if status == 'left':
                    tempS = min(s,start)
                status = 'mid'
            if status == 'mid':
                tempE = max(e,end)
            else:
                answer.append([s,e])
        if status == 'mid':
            answer.append([tempS, tempE])
        elif status == 'left':
            answer.append(newInterval)
        return answer