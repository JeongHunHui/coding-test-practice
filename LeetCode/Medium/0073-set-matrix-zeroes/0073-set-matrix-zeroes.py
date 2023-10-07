class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xLen, yLen = len(matrix[0]), len(matrix)
        xSet, ySet = set(), set()
        for y in range(yLen):
            for x in range(xLen):
                if matrix[y][x] == 0:
                    xSet.add(x)
                    ySet.add(y)
        for x in xSet:
            for y in range(yLen):
                matrix[y][x] = 0
        for y in ySet:
            for x in range(xLen):
                matrix[y][x] = 0