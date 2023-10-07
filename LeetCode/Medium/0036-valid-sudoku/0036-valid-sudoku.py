class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxSet, rowSet, colSet = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for y in range(9):
            row = board[y]
            for x in range(9):
                num = row[x]
                if num == '.':
                    continue
                boxNum = y//3*3+x//3
                if num in rowSet[y] or num in colSet[x] or num in boxSet[boxNum]:
                    return False
                rowSet[y].add(num)
                colSet[x].add(num)
                boxSet[boxNum].add(num)
        return True