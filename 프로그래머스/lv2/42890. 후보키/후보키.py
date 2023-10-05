from itertools import combinations as comb
def solution(relation):
    colCount = len(relation[0])
    rowCount = len(relation)
    cKeys = set()
    for i in range(colCount):
        combs = [c for c in comb(range(colCount),i+1) if all(not set(key).issubset(set(c)) for key in cKeys)]
        for c in combs:
            checkSet = set()
            for row in relation:
                arr = []
                for i in c:
                    arr.append(row[i])
                checkSet.add(tuple(arr))
            if len(checkSet) == rowCount:
                cKeys.add(c)
    return len(cKeys)