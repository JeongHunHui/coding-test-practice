from collections import Counter
def solution(topping):
    answer = 0
    toppingCounter = Counter(topping)
    leftCount = len(toppingCounter.keys())
    toppingSet = set()
    for i in topping:
        toppingSet.add(i)
        toppingCounter[i] -= 1
        if toppingCounter[i] == 0:
            leftCount -= 1
        if len(toppingSet) == leftCount:
            answer += 1
    return answer