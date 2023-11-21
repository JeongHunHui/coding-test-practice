class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def search(node, val):
            nonlocal answer
            new_val = val * 10 + node.val
            if node.left == None and node.right == None:
                answer += new_val
                return
            if node.left:
                search(node.left, new_val)
            if node.right:
                search(node.right, new_val)
        search(root, 0)
        return answer