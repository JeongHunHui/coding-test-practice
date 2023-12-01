import math

def solution(n, results):
    rank_info_down = [[math.inf]*(n) for _ in range(n)]
    rank_info_up = [[math.inf]*(n) for _ in range(n)]
    for a,b in results:
        rank_info_down[a-1][b-1] = 1
        rank_info_up[b-1][a-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                rank_info_down[i][j] = min(rank_info_down[i][j], rank_info_down[i][k]+rank_info_down[k][j])
                rank_info_up[i][j] = min(rank_info_up[i][j], rank_info_up[i][k]+rank_info_up[k][j])
    
    count = 0        
    for i in range(n):
        if sum([1 for j in range(n) if rank_info_down[i][j] != math.inf]) + sum([1 for j in range(n) if rank_info_up[i][j] != math.inf]) == n-1:
            count += 1
    
    return count