from collections import deque
class Node:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.child:
                curr_node.child[c] = Node()
            curr_node = curr_node.child[c]
        curr_node.is_end = True
    
    def dfs(self, node, word):
        if word == '':
            return node.is_end
        c = word[0]
        new_word = word[1:]
        if c in node.child:
            return self.dfs(node.child[c], new_word)
        if c == '.':
            for k, n in node.child.items():
                if self.dfs(n, new_word):
                    return True
        return False

    def search(self, word: str) -> bool:
        is_exist = self.dfs(self.root, word)
        return is_exist