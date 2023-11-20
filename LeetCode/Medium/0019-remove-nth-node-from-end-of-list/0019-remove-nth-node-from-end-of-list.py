# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right_node = head
        left_node = head
        for i in range(n):
            right_node = right_node.next
        if right_node == None:
            return head.next
        while right_node.next:
            right_node = right_node.next
            left_node = left_node.next
        left_node.next = left_node.next.next
        return head