is_visited = []
answer = 0

def dfs(depth, k, dungeons):
    global answer
    if depth == len(dungeons):
        return
    for i in range(0,len(dungeons)):
        if is_visited[i]:
            continue
        dungeon = dungeons[i]
        if k >= dungeon[0] and k-dungeon[1] >= 0:
            if answer < depth + 1:
                answer = depth + 1
            is_visited[i] = True
            dfs(depth+1, k-dungeon[1], dungeons)
            is_visited[i] = False

def solution(k, dungeons):
    global is_visited
    is_visited = [False for i in range(0,len(dungeons))]
    dfs(0, k, dungeons);
    return answer