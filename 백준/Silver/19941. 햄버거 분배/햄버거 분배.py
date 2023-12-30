# 09:28
n, k = map(int, input().split())
infos = [c for c in input()]
h_stack = []
p_stack = []
for i, c in enumerate(infos):
    if c == 'H':
        h_stack = [i] + h_stack
    else:
        p_stack = [i] + p_stack
def calculate_person():
    # 햄버거가 사람보다 오른쪽에 있는데, 먹을 수 없으면 p_stack pop
    if not h_stack or not p_stack:
        return 0
    current_p = p_stack.pop()
    current_h = h_stack.pop()
    count = 0
    while True:
        diff = current_p - current_h
        if abs(diff) <= k:
            count += 1
            if not h_stack or not p_stack:
                break
            current_p = p_stack.pop()
            current_h = h_stack.pop()
            continue
        if diff > 0:
            if not h_stack:
                break
            current_h = h_stack.pop()
        else:
            if not p_stack:
                break
            current_p = p_stack.pop()
    return count
print(calculate_person())