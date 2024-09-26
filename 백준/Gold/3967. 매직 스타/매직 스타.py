#02:51
board = [list(input()) for _ in range(5)]
posList = []
abcSet = set(chr(ord('A') + i) for i in range(12))
used = set()

for i in range(5):
    for j in range(9):
        if board[i][j] == 'x':
            posList.append((i, j))
        elif board[i][j].isalpha():
            used.add(board[i][j])

left = list(abcSet - used)

lines = [
    [(0, 4), (1, 3), (2, 2), (3, 1)],
    [(0, 4), (1, 5), (2, 6), (3, 7)],
    [(1, 1), (1, 3), (1, 5), (1, 7)],
    [(3, 1), (3, 3), (3, 5), (3, 7)],
    [(4, 4), (3, 3), (2, 2), (1, 1)],
    [(4, 4), (3, 5), (2, 6), (1, 7)]
]

def early_stop():
    for line in lines:
        total = 0
        for x, y in line:
            if board[x][y] == 'x':
                continue
            total += ord(board[x][y]) - ord('A') + 1
        if total > 26:
            return True
    return False

def check():
    for line in lines:
        total = sum(ord(board[x][y]) - ord('A') + 1 for x, y in line)
        if total != 26:
            return False
    return True

def go(depth, used_chars):
    if early_stop():
        return False
    if depth == len(posList):
        if check():
            for row in board:
                print(''.join(row))
            return True
        return False
    
    x, y = posList[depth]
    for c in sorted(left):
        if c in used_chars:
            continue
        board[x][y] = c
        used_chars.add(c)
        if go(depth + 1, used_chars):
            return True
        used_chars.remove(c)
        board[x][y] = 'x'
    return False

go(0, set())
