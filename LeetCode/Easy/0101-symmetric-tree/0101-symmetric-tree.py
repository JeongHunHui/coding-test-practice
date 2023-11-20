# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        is_symmetric = True
        def search(left, right):
            nonlocal is_symmetric
            if not is_symmetric:
                return
            if left and right:
                if left.val != right.val:
                    is_symmetric = False
                    return
                search(left.left, right.right)
                search(left.right, right.left)
                return
            if left == None and right == None:
                return
            is_symmetric = False
            return
        search(root.left, root.right)
        return is_symmetric