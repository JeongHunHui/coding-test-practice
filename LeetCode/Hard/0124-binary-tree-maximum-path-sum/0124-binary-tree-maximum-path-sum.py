import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 트리를 순회하면서 최대값 갱신
        # 대신, path가 될수 있도록(일직선으로 이동할 수 있게 -> root만 두 갈래가 되도록)
        max_val = -math.inf
        def search(node):
            nonlocal max_val
            if not node:
                return 0
            left_val = search(node.left)
            right_val = search(node.right)
            c_max_val = max(left_val + node.val, right_val + node.val, node.val)
            max_val = max(c_max_val, max_val, left_val + right_val + node.val)
            return c_max_val
        search(root)
        return max_val