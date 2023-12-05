class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 현재 탐색중인 노드를 가리키는 포인터
        currNode = self.root
        # 삽입한 word를 순회하며
        for ch in word:
            # 현재 노드의 childNodes 중 키가 ch인 노드가 있으면 이동, 없으면 생성
            node = currNode.childNodes.get(ch , TrieNode())
            currNode.childNodes[ch] = node
            currNode = node
        # 하나의 단어를 끝까지 넣었다면 해당 노드의 isWordEnd를 True로 변경
        currNode.isWordEnd = True

    def search(self, word: str) -> bool:
        # 현재 탐색중인 노드를 가리키는 포인터
        currNode = self.root
        for ch in word:
            if ch not in currNode.childNodes:
                return False
            currNode = currNode.childNodes[ch]
        # 목적지 노드가 단어의 끝이면 True Return
        return currNode.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        # search와 거의 같지만, 마지막에 isWordEnd와 상관없이 True Return
        currNode = self.root
        for ch in prefix:
            if ch not in currNode.childNodes:
                return False
            currNode = currNode.childNodes[ch]
        return True