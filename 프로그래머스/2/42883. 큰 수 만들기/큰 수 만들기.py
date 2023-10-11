def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and k > 0:
            if stack[len(stack)-1] >= num:
                break
            stack.pop()
            k -= 1
        stack.append(num)
    if k == 1: stack.pop()
    return ''.join(stack)