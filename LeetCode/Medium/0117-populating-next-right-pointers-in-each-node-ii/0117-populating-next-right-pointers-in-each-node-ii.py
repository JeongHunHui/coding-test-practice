"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import defaultdict
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node_dict = defaultdict(list)
        def search(node, depth):
            if not node:
                return
            node_dict[depth].append(node)
            search(node.left, depth+1)
            search(node.right, depth+1)
        search(root, 1)
        for nodes in node_dict.values():
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
        return root