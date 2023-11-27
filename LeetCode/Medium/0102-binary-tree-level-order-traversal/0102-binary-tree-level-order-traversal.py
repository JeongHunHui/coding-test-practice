# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        value_dict = defaultdict(list)
        def search(node, depth):
            if not node:
                return
            value_dict[depth].append(node.val)
            search(node.left, depth+1)
            search(node.right, depth+1)
        search(root,0)
        i = 0
        answer = []
        while i in value_dict:
            answer.append(value_dict[i])
            i += 1
        return answer