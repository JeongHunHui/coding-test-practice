# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def search(inorder):
            if not inorder:
                return None
            val = postorder.pop(0)
            i = inorder.index(val)
            left, right = inorder[:i], inorder[i+1:]
            right_node = search(right)
            left_node = search(left)
            return TreeNode(val, left_node, right_node)
        postorder = postorder[::-1]
        return search(inorder)