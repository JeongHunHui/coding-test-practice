class Solution:
    def trap(self, height: List[int]) -> int:
        # 가장 높은 곳들의 index들을 구함
        # 가장 높은 곳이 | 라고하면
        # [ 왼쪽 > 높은 곳 탐색 -> | 중간 부분 탐색 -> | <- 오른쪽 > 높은 곳 탐색 ]
        l = len(height)
        answer, max_h, left_i, right_i = 0, -1, -1, -1

        for i in range(l):
            cur_h = height[i]
            if cur_h > max_h:
                max_h = cur_h
                left_i = i
                right_i = i
            elif cur_h == max_h:
                right_i = i
        
        c_max_h = 0
        for i in range(left_i):
            cur_h = height[i]
            if cur_h > c_max_h:
                c_max_h = cur_h
            else:
                answer += c_max_h-cur_h
        
        c_max_h = 0
        for i in range(l-1, right_i-1, -1):
            cur_h = height[i]
            if cur_h > c_max_h:
                c_max_h = cur_h
            else:
                answer += c_max_h-cur_h

        for i in range(left_i+1, right_i):
            answer += max_h-height[i]
        
        return answer
            