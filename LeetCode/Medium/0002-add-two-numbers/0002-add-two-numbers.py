class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        numStr = str(num1 + num2)
        answer = ListNode(numStr[0], None)
        for c in numStr[1:]:
            answer = ListNode(c, answer)
        return answer