class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def divide(node):
            p, slow, fast = None, node, node
            while fast and fast.next:
                p = slow
                slow = slow.next
                fast = fast.next.next
            p.next = None
            return node, slow
        
        def merge(left, right):
            dummy = ListNode(None)
            current = dummy
            while left and right:
                if left.val > right.val:
                    current.next = right
                    right = right.next
                else:
                    current.next = left
                    left = left.next
                current = current.next
            if left:
                current.next = left
            elif right:
                current.next = right
            return dummy.next
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            left, right = divide(head)
            return merge(merge_sort(left), merge_sort(right))

        return merge_sort(head)