from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeStrCode(s):
            counter = Counter(s)
            answer = ''
            for c in sorted(list(set(s))):
                answer += f'{c}{counter[c]}'
            return answer
        codeDict = defaultdict(list)
        for i in range(len(strs)):
            codeDict[makeStrCode(strs[i])].append(i)
        keys = list(codeDict.keys())
        keys.sort(key=lambda k: len(codeDict[k]))
        return [sorted([strs[i] for i in codeDict[key]]) for key in keys]
