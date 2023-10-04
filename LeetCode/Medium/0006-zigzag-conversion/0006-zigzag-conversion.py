from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = ['']*numRows
        diff = 0
        i=0
        s_que = deque(s)
        while s_que:
            c = s_que.popleft()
            arr[i] += c
            if i == numRows - 1:
                diff = -1
            elif i == 0:
                diff = 1
            i += diff
        return ''.join(arr)