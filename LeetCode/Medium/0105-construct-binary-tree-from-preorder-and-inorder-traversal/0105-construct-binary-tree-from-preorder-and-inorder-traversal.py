# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def search(inorder):
            if not inorder:
                return None
            root_val = preorder.pop(0)
            i = inorder.index(root_val)
            left, right = inorder[:i], inorder[i+1:]
            return TreeNode(root_val, search(left), search(right))
        return search(inorder)