import heapq
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        def search(node):
            if not node:
                return
            heapq.heappush(self.values, node.val)
            search(node.left)
            search(node.right)
        search(root)
    def next(self) -> int:
        return heapq.heappop(self.values)
    def hasNext(self) -> bool:
        return len(self.values) > 0