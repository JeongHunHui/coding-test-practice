def solution(n, lost, reserve):
    lost_set = set(lost)-set(reserve)
    reserve_set = set(reserve)-set(lost)
    answer = n-len(lost_set)
    
    for i in lost_set:
        if i-1 in reserve_set:
            reserve_set.remove(i-1)
            answer += 1
            continue
        if i+1 in reserve_set:
            reserve_set.remove(i+1)
            answer += 1
            continue
    return answer