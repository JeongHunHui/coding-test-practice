from collections import defaultdict, deque

class TreeNode:
    def __init__(self):
        self.child = dict()
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # words를 트리로 만든다.
        root = TreeNode()
        for word in words:
            current_node = root
            for c in word:
                if c not in current_node.child:
                    current_node.child[c] = TreeNode()
                current_node = current_node.child[c]
            current_node.is_end = True

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        x_len = len(board[0])
        y_len = len(board)
        answer = set()
        is_visited = [[False] * x_len for _ in range(y_len)]

        # 시작 좌표를 기준으로 dfs, tree도 함께 따라가며 탐색
        def dfs(x, y, node, word):
            if node.is_end:
                answer.add(word)
            if len(node.child.keys()) == 0:
                return
            is_visited[y][x] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < x_len and ny >= 0 and ny < y_len and not is_visited[ny][nx]:
                    c = board[ny][nx]
                    for key, value in node.child.items():
                        if c == key:
                            dfs(nx, ny, value, word+c)
            is_visited[y][x] = False
        
        # 모든 점을 시작점으로 탐색
        words_count = len(words)
        for y in range(y_len):
            for x in range(x_len):
                if words_count == len(answer):
                    break
                c = board[y][x]
                if c in root.child.keys():
                    is_visited = [[False] * x_len for _ in range(y_len)]
                    dfs(x,y,root.child[c],c)
        
        return list(answer)