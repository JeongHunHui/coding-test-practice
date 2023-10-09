class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordCounter = Counter(words)
        size = len(words[0])
        allLen = size * len(words)
        def isSubstr(substr):
            counter = copy.deepcopy(wordCounter)
            for i in range(0,allLen,size):
                word = substr[i:i+size]
                if word not in counter or counter[word] == 0:
                    return False
                counter[word] -= 1
            return True
        answer = []
        for i in range(len(s) - allLen + 1):
            if isSubstr(s[i:i+allLen]):
                answer.append(i)
        return answer