# 11:42
brackets = {'(', ')', '[', ']'}
brackets_dict = {'(': ')', '[': ']'}
inputs = []
s = input()
while s != '.':
    temp = [c for c in s if c in brackets]
    temp.reverse()
    inputs.append(temp)
    s = input()
inputs.reverse()
while inputs:
    temp = inputs.pop()
    stack = []
    while temp:
        bracket = temp.pop()
        if stack and stack[-1] in brackets_dict.keys() and brackets_dict[stack[-1]] == bracket:
            stack.pop()
        else:
            stack.append(bracket)
    if stack:
        print('no')
    else:
        print('yes')