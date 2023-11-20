# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def find(node, depth):
            nonlocal max_depth
            if not node:
                max_depth = max(depth, max_depth)
                return
            find(node.left, depth+1)
            find(node.right, depth+1)
        find(root, 0)
        return max_depth