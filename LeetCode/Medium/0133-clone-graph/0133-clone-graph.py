from typing import Optional

from collections import deque, defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def bfs(start_node):
            node_dict = defaultdict(list)
            que = deque()
            que.append(start_node)
            while que:
                node = que.popleft()
                val = node.val
                if val in node_dict:
                    continue
                for neighbor in node.neighbors:
                    node_dict[val].append(neighbor.val)
                    que.append(neighbor)
            return node_dict
        
        node_dict = bfs(node)
        nodes = []
        for i in range(len(node_dict)):
            nodes.append(Node(i+1,[]))
        
        for key, values in node_dict.items():
            for val in values:
                nodes[key-1].neighbors.append(nodes[val-1])
        
        return nodes[0] if nodes else Node(1,[])
