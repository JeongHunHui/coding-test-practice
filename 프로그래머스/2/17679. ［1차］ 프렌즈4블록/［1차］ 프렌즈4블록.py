def solution(m, n, board):
    temp_board = [[c2 for c2 in c] for c in board]
    main_board = [[c2 for c2 in c] for c in board]
    
    def get_rect_set(r,c):
        block = main_board[r][c]
        if r+1 >= m or c+1 >= n or block == ' ':
            return set()
        return set([(r,c),(r+1,c),(r,c+1),(r+1,c+1)]) if block == main_board[r+1][c] == main_board[r][c+1] == main_board[r+1][c+1] else set()
    
    while True:
        new_set = set()
        for r in range(m):
            for c in range(n):
                new_set = new_set | get_rect_set(r, c)
                
        if len(new_set) == 0:
            break
            
        for s in new_set:
            temp_board[s[0]][s[1]] = ' '
            
        for c in range(m):
            for r in range(n-2,-1,-1):
                for i in range(r, len(temp_board)-1):
                    down_block = temp_board[i+1][c]
                    if down_block == ' ':
                        temp_board[i+1][c] = temp_board[i][c]
                        temp_board[i][c] = ' '
        
        main_board = temp_board

    return sum([board.count(' ') for board in temp_board])