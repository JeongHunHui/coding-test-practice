class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        value_dict = defaultdict(list)
        def search(node, depth):
            if not node:
                return
            value_dict[depth].append(node.val)
            search(node.left, depth+1)
            search(node.right, depth+1)
        search(root,0)
        i = 0
        answer = []
        while i in value_dict:
            values = value_dict[i] if i % 2 == 0 else reversed(value_dict[i])
            answer.append(values)
            i += 1
        return answer