class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        headSet = {}
        while head:
            if head in headSet:
                return True
            headSet[head] = True
            head = head.next
        return False