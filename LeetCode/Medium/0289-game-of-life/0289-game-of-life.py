class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        xLen, yLen = len(board[0]), len(board)
        countBoard = [[0] * xLen for i in range(yLen)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        def isInBoard(x,y):
            return x >= 0 and x < xLen and y >= 0 and y < yLen
            
        def updateCount(x,y):
            posList = [(x+xDir,y+yDir) for xDir, yDir in dirs if isInBoard(x+xDir,y+yDir)]
            for xPos, yPos in posList:
                countBoard[yPos][xPos] += 1

        for y in range(yLen):
            for x in range(xLen):
                if board[y][x] == 1:
                    updateCount(x,y)
                    
        for y in range(yLen):
            for x in range(xLen):
                count = countBoard[y][x]
                if board[y][x] == 0:
                    if count == 3:
                        board[y][x] = 1
                    else:
                        board[y][x] = 0
                elif count < 2 or count > 3:
                    board[y][x] = 0
                else:
                    board[y][x] = 1