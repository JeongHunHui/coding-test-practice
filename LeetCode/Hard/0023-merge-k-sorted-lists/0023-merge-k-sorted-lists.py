# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide(lists):
            mid = len(lists)//2
            return lists[:mid], lists[mid:]
        def merge(left, right):
            dummy = ListNode()
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
        def merge_lists(lists):
            if len(lists) == 1:
                return lists[0]
            if not lists:
                return None
            left, right = divide(lists)
            return merge(merge_lists(left), merge_lists(right))
        return merge_lists(lists)
