def solution(triangle):
    l = len(triangle)
    for h in range(1, l):
        triangle[h][0] += triangle[h-1][0]
        for i in range(1, h):
            triangle[h][i] += max(triangle[h-1][i-1], triangle[h-1][i])
        triangle[h][h] += triangle[h-1][h-1]
    return max(triangle[l-1])
