class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cCounter = Counter(t)
        start, answer, needCount = 0, (0,len(s)+1), len(t)
        for end, c in enumerate(s):
            if c not in cCounter:
                continue
            if cCounter[c] > 0:
                needCount -= 1
            cCounter[c] -= 1
            if needCount == 0:
                while True:
                    temp = s[start]
                    if temp not in cCounter:
                        start += 1
                        continue
                    if cCounter[temp] == 0:
                        break
                    cCounter[temp] += 1
                    start += 1
                if end - start < answer[1] - answer[0]:
                    answer = (start, end)
                cCounter[s[start]] += 1
                needCount += 1
                start += 1
        return '' if answer[1] > len(s) else s[answer[0]:answer[1]+1]