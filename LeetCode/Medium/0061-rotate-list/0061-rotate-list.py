# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 끝이랑 시작을 연결, 중간 끊기
        temp = head
        count = 1
        if not temp:
            return None
        while temp.next:
            count += 1
            temp = temp.next
        n = count - k % count
        if n == 0 or n == count:
            return head
        tail = head
        for i in range(n-1):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        temp.next = head
        return new_head