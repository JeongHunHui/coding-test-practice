import copy
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        answer = TreeNode(root.val, None, None)
        tail = answer
        def search(node):
            nonlocal tail
            if not node:
                return
            tail.right = TreeNode(node.val, None, None)
            tail = tail.right
            search(node.left)
            search(node.right)
        search(root)
        root.right = answer.right.right
        root.left = None