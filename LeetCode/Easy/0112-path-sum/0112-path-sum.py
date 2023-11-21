# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        answer = False
        def search(node, val):
            nonlocal answer
            if node and node.left == None and node.right == None:
                if val + node.val == targetSum:
                    answer = True
                return
            if node.left:
                search(node.left, val + node.val)
            if node.right:
                search(node.right, val + node.val)
        search(root, 0)
        return answer
