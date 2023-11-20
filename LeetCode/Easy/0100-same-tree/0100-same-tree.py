# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        search_finish = False
        def search(node1, node2):
            nonlocal search_finish
            if search_finish:
                return
            if node1 and node2:
                if node1.val != node2.val:
                    search_finish = True
                    return
                search(node1.left, node2.left)
                search(node1.right, node2.right)
            elif node1 == None and node2 == None:
                return
            else:
                search_finish = True
                return
        search(p,q)
        return not search_finish