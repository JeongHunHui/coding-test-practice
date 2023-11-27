class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 현재 노드가 p or q or None이면 return, 아니면 left와 right 탐색
        pq_set = set([p.val, q.val])
        def search(node):
            if not node or node.val in pq_set:
                return node
            left = search(node.left)
            right = search(node.right)
            if left and right:
                return node
            return left or right
        return search(root)
        