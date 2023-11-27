class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None
        def search(node):
            nonlocal count, answer
            if not node or answer:
                return
            search(node.left)
            count += 1
            if count == k:
                answer = node.val
            search(node.right)
        search(root)
        return answer