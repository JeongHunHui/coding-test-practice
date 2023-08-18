def is_tree_correct(skill, my_skill):
    for i in range(len(my_skill)):
        if skill[i] != my_skill[i]:
            return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        my_skill = ""
        for s in skill_tree:
            if s in skill:
                my_skill += s
        if is_tree_correct(skill, my_skill):
            answer += 1
    return answer