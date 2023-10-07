class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xCount, yCount = len(matrix[0]), len(matrix)-1
        moveDirs = [(1,0),(0,1),(-1,0),(0,-1)] # (가로 변화량, 세로 변화량)
        dirNum = 0
        x, y = -1, 0
        answer = []
        while True:
            xDir, yDir = moveDirs[dirNum%4]
            count = None
            # 가로 이동
            if xDir != 0:
                count = xCount
                xCount -= 1
            # 세로 이동
            else:
                count = yCount
                yCount -= 1
            if count == 0:
                break
            for i in range(count):
                x += xDir
                y += yDir
                answer.append(matrix[y][x])
            dirNum += 1
        return answer