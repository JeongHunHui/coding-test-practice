# 17:15
def solution(triangle):
    height = len(triangle)
    answers = [[-1] * len(values) for values in triangle]
    answers[0][0] = triangle[0][0]
    for depth in range(1, height):
        for i, val in enumerate(triangle[depth]):
            left_parent = 0 if i == 0 else answers[depth-1][i-1]
            right_parent = 0 if i == depth else answers[depth-1][i]
            answers[depth][i] = max(left_parent, right_parent) + val
    return max(answers[height-1])
            