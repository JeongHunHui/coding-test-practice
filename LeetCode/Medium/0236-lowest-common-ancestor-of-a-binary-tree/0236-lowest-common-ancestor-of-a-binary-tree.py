class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_values = None
        q_values = None
        def search(node, values):
            nonlocal p_values, q_values
            if not node or (p_values and q_values):
                return
            current_value = node.val
            new_values = values + [node]
            if current_value == p.val:
                p_values = new_values
            if current_value == q.val:
                q_values = new_values
            search(node.left, new_values)
            search(node.right, new_values)
        search(root, [])
        common_elements = set([node.val for node in p_values]) & set([node.val for node in q_values])
        for element in reversed(p_values if len(p_values) < len(q_values) else q_values):
            if element.val in common_elements:
                return element