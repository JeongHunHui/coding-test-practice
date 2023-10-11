def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        new_tree = ''.join([c for c in tree if c in skill])
        if new_tree == skill[:len(new_tree)]:
            answer += 1
    return answer