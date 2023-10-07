class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        answer = [[0]*n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                answer[y][x] = matrix[n-x-1][y]
        matrix[:] = answer