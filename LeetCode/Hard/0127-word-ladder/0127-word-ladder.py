from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord)
        def make_temp_word(word, i):
            return word[:i] + '*' + word[i+1:]
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(l):
                word_dict[make_temp_word(word,i)].append(word)
        use_word_set = {beginWord}
        que = deque([[1,beginWord]])
        while que:
            count, word = que.popleft()
            for i in range(l):
                for w in word_dict[make_temp_word(word,i)]:
                    if w in use_word_set:
                        continue
                    if w == endWord:
                        return count+1
                    use_word_set.add(w)
                    que.append([count+1, w])
        return 0