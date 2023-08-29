from collections import deque

def get_move_pos_list(x, y):
    return [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]

def solution(maps):
    row = len(maps[0])
    col = len(maps)
    
    visited = [[False for _ in range(row)] for _ in range(col)]
    
    def can_visit(x, y, count):
        return x >= 0 and x < row and y >= 0 and y < col and not visited[y][x] and (maps[y][x] == 1 or maps[y][x] == count)
    
    def is_opposite(x, y):
        return x == row-1 and y == col-1
        
    queue = deque([(0,0,2)])
    while queue:
        x, y, count = queue.popleft()
        move_pos_list = get_move_pos_list(x, y)
        for new_x, new_y in move_pos_list:
            if can_visit(new_x, new_y, count):
                if is_opposite(new_x, new_y):
                    return count
                maps[new_y][new_x] = count + 1
                visited[new_y][new_x] = True
                queue.append((new_x, new_y, count+1))
    return -1