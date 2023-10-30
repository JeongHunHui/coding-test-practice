# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        node1, node2, values = list1, list2, []
        while node1 or node2:
            if not node2:
                values.append(node1.val)
                node1 = node1.next
            elif not node1:
                values.append(node2.val)
                node2 = node2.next
            elif node1.val <= node2.val:
                values.append(node1.val)
                node1 = node1.next
            else:
                values.append(node2.val)
                node2 = node2.next
        values = values[::-1]
        answer = ListNode(values[0], None)
        for i in values[1:]:
            answer = ListNode(i, answer)
        return answer