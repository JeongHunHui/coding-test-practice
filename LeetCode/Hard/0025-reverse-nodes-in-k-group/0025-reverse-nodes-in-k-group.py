# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values, temp = [], []
        count = 0
        while head:
            temp.append(head.val)
            head = head.next
            count += 1
            if count == k:
                values += temp[::-1]
                temp = []
                count = 0
        if len(temp) > 0:
            values += temp
        
        values = values[::-1]
        answer = ListNode(values[0], None)
        for val in values[1:]:
            answer = ListNode(val, answer)
        return answer