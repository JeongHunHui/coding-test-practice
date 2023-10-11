move_dict = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
def move(direction, current_pos):
    x, y = current_pos
    dx, dy = move_dict[direction]
    new_x = x + dx
    new_y = y + dy
    x = x if new_x > 5 or new_x < -5 else new_x
    y = y if new_y > 5 or new_y < -5 else new_y
    return (x, y)

def solution(dirs):
    answer = 0
    current_pos = (0,0)
    moving_records = []
    for direction in dirs:
        new_pos = move(direction, current_pos)
        if new_pos != current_pos:
            moving_record = sorted([current_pos, new_pos])
            moving_records.append((moving_record[0], moving_record[1]))
            current_pos = new_pos
    return len(set(moving_records))