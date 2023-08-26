def solution(land):
    len_1, len_2 = len(land), len(land[0])
    for i in range(1, len_1):
        for j in range(len_2):
            land[i][j] += max([land[i-1][k] for k in range(len_2) if k != j])
    return max(land[len_1-1])