# 23:40
from collections import defaultdict, deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    edge_set = set()
    edge_dict = defaultdict(list)
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2):
            edge_set.add((x,y1,x+1,y1))
            edge_set.add((x,y2,x+1,y2))
        for y in range(y1, y2):
            edge_set.add((x1,y,x1,y+1))
            edge_set.add((x2,y,x2,y+1))
    
    for x1, y1, x2, y2 in rectangle:
        remove_edges = []
        for nx1, ny1, nx2, ny2 in edge_set:
            # 간선이 사각형 안에 포함되면 삭제
            if x1 <= nx1 <= x2 and y1 <= ny1 <= y2 and x1 <= nx2 <= x2 and y1 <= ny2 <= y2:
                if nx1 == nx2 and nx1 != x1 and nx1 != x2:
                    remove_edges.append((nx1, ny1, nx2, ny2))
                elif ny1 == ny2 and ny1 != y1 and ny1 != y2:
                    remove_edges.append((nx1, ny1, nx2, ny2))
        for edge in remove_edges:
            edge_set.remove(edge)
    
    for x1, y1, x2, y2 in edge_set:
        edge_dict[f'{x1},{y1}'].append(f'{x2},{y2}')
        edge_dict[f'{x2},{y2}'].append(f'{x1},{y1}')
        
    character_pos = f'{characterX},{characterY}'
    item_pos = f'{itemX},{itemY}'
    
    visited_set = set()
    answers = []
    
    que = deque([(character_pos, 0)])
    while que:
        pos, distance = que.popleft()
        if pos == item_pos:
            answers.append(distance)
            continue
        visited_set.add(pos)
        for node in edge_dict[pos]:
            if node not in visited_set:
                que.append((node, distance+1))
    
    return min(answers)