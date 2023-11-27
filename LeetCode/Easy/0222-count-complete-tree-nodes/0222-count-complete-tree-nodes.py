class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        def search(node):
            nonlocal count
            if not node:
                return
            count += 1
            search(node.left)
            search(node.right)
        search(root)
        return count