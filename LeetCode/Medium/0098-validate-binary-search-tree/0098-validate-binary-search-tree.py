class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        pre_val = None
        def search(node):
            nonlocal is_valid, pre_val
            if not node or not is_valid:
                return
            search(node.left)
            if pre_val != None and pre_val >= node.val:
                is_valid = False
                return
            pre_val = node.val
            search(node.right)
        search(root)
        return is_valid