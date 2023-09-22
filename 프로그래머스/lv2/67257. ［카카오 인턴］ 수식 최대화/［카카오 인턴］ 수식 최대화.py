from itertools import permutations
import re

def solution(expression):
    answer = 0
    operators_list = list(permutations('*+-',3))
    elements = re.findall(r'\d+|[*+-]', expression)
    for i in range(0,len(elements),2):
        elements[i] = int(elements[i])
    for op in operators_list:
        n_elements = elements[:]
        for o in op:
            i = 0
            while i < len(n_elements):
                e = n_elements[i]
                if o == e:
                    if o == '*':
                        n_elements[i-1] *= n_elements[i+1]
                    elif o == '+':
                        n_elements[i-1] += n_elements[i+1]
                    elif o == '-':
                        n_elements[i-1] -= n_elements[i+1]
                    n_elements = n_elements[:i] + n_elements[i+2:]
                else:
                    i += 1
        answer = max(answer, abs(int(n_elements[0])))
    return answer