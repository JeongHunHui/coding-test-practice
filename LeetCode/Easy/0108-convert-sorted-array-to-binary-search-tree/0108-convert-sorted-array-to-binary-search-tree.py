class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(node, nums, is_left):
            if len(nums) == 0:
                return
            mid = len(nums)//2
            current_node = TreeNode(val=nums[mid])
            if is_left:
                node.left = current_node
            else:
                node.right = current_node
            dfs(current_node, nums[:mid], True)
            dfs(current_node, nums[mid+1:], False)
        mid = len(nums)//2
        root = TreeNode(val=nums[mid])
        dfs(root, nums[:mid], True)
        dfs(root, nums[mid+1:], False)
        return root