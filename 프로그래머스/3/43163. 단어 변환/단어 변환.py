from collections import deque

def solution(begin, target, words):
    word_len = len(target)
    
    def can_translate(word, target):
        return sum([1 for i in range(word_len) if word[i] == target[i]]) == word_len-1
    
    def bfs():
        que = deque()
        que.append((begin, 0, set()))
        while que:
            word, depth, word_set = que.popleft()
            if word == target:
                return depth
            for w in words:
                if w not in word_set and can_translate(word, w):
                    que.append((w,depth+1,word_set|{w}))
        return 0
            
    return bfs()