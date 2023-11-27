import math
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = math.inf
        pre_val = None
        def search(node):
            nonlocal min_diff, pre_val
            if not node:
                return
            search(node.left)
            if pre_val != None:
                min_diff = min(abs(pre_val - node.val), min_diff)
            pre_val = node.val
            search(node.right)
        search(root)
        return min_diff