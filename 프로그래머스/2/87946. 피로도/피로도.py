from itertools import permutations

def explore_count(k, dungeon):
    count = 0
    for li in dungeon:
        min_k, con_k = li
        if min_k > k:
            break
        count += 1
        k -= con_k
    return count

def solution(k, dungeons):
    dungeons = list(permutations(dungeons))
    dungeon_count = len(dungeons)
    max_explore_count = 0
    for dungeon in dungeons:
        max_explore_count = max(max_explore_count, explore_count(k, dungeon))
        if max_explore_count == dungeon_count:
            return max_explore_count
    return max_explore_count