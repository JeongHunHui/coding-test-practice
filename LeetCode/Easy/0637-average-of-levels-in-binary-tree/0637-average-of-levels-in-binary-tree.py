from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        value_dict = defaultdict(list)
        def search(node, depth):
            if not node:
                return
            value_dict[depth].append(float(node.val))
            search(node.left, depth+1)
            search(node.right, depth+1)
        search(root, 0)
        i = 0
        answer = []
        while i in value_dict:
            answer.append(sum(value_dict[i]) / len(value_dict[i]))
            i += 1
        return answer