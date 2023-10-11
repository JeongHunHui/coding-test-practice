from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        count = 1
        queue = deque([start])
        is_visited = [False for i in range(0, n+1)]
        is_visited[start] = True
        while queue:
            i = queue.popleft()
            for num in graph[i]:
                if not is_visited[num]:
                    is_visited[num] = True
                    queue.append(num)
                    count += 1
        return count
    
    answer = n
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer