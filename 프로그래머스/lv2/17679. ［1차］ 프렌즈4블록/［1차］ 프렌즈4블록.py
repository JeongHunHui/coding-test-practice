def solution(m, n, board):
    temp_board = [[c2 for c2 in c] for c in board]
    main_board = [[c2 for c2 in c] for c in board]
    
    def check_rect(r,c):
        block = main_board[r][c]
        new_set = set()
        if r+1 >= m or c+1 >= n or block == ' ': return new_set
        if block == main_board[r+1][c] and block == main_board[r][c+1] and block == main_board[r+1][c+1]:
            new_set.add((r,c))
            new_set.add((r+1,c))
            new_set.add((r,c+1))
            new_set.add((r+1,c+1))
            return new_set
        else: return new_set
    
    is_changed = True
    count = 0
    while is_changed:
        new_set = set()
        for r in range(m):
            for c in range(n):
                new_set = new_set | check_rect(r, c)
        if len(new_set) == 0: break
        for s in new_set:
            temp_board[s[0]][s[1]] = ' '
            
        for c in range(len(temp_board[0])):
            for r in range(len(temp_board)-2,-1,-1):
                for i in range(r, len(temp_board)-1):
                    down_block = temp_board[i+1][c]
                    if down_block == ' ':
                        temp_board[i+1][c] = temp_board[i][c]
                        temp_board[i][c] = ' '
        
        main_board = temp_board

    answer = 0
    for board in temp_board:
        for block in board:
            if block == ' ':
                answer += 1
    return answer