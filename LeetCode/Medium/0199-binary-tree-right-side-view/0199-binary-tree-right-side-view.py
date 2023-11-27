from collections import OrderedDict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_values = OrderedDict()
        def search(node, depth):
            if not node:
                return
            right_values[depth] = node.val
            search(node.left, depth+1)
            search(node.right, depth+1)
        search(root, 0)
        return list(right_values.values())