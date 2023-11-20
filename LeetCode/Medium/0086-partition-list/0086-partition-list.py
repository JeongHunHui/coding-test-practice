# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        less_x_head = None
        less_x_tail = None
        other_head = None
        other_tail = None
        while temp:
            if temp.val < x:
                if less_x_head:
                    less_x_tail.next = temp
                    less_x_tail = temp
                else:
                    less_x_head = temp
                    less_x_tail = temp
            else:
                if other_head:
                    other_tail.next = temp
                    other_tail = temp
                else:
                    other_head = temp
                    other_tail = temp
            temp = temp.next
        if not less_x_head:
            return other_head
        if not other_head:
            return less_x_head
        less_x_tail.next = other_head
        other_tail.next = None
        return less_x_head