# 01:21
# 마지막 방 가지 살아남을 수 있는 최소한의 최대 생명력 계산하기

import math

# 방 개수, 공격력
n, atk = map(int, input().split())
# 각 방 정보(t, a, h)
# t == 1 -> a = 몬스터 공격력, b = 몬스터 체력
# t == 2 -> a = 용사 공격력 증가, b = 용사 체력 회복
rooms = [tuple(map(int, input().split())) for _ in range(n)]

# 전투 진행
# 1. atk만큼 몬스터 생명력 -
# 2. 몬스터 죽으면 다음방, 몬스터 살아있으면 몬스터 atk 만큼 용사 생명력 -

# 용사 체력은 최소 1 ~ 최대 모르겠네

def can_survive(max_hp):
    c_hp = max_hp
    c_atk = atk
    for t, a, h in rooms:
        if t == 2:
            c_atk += a
            c_hp = min(c_hp+h, max_hp)
            continue
        max_damage = int(math.ceil(h / c_atk)-1) * a
        c_hp -= max_damage
        if c_hp <= 0:
            return False
    return True

def get_max_damage():
    max_damage = 0
    for t, a, h in rooms:
        if t == 1:
            max_damage += int(math.ceil(h / atk)) * a
    return max_damage

left, right = 1, get_max_damage()
answer = right
while left <= right:
    mid = (left+right)//2
    if can_survive(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)