class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        valuesLeft = []
        valuesMid = []
        valuesRight = []
        index = 1
        while head:
            if index < left:
                valuesLeft.append(head.val)
            elif index > right:
                valuesRight.append(head.val)
            else:
                valuesMid.append(head.val)
            head = head.next
            index += 1
        values = valuesRight[::-1] + valuesMid + valuesLeft[::-1]
        answer = ListNode(values[0], None)
        for val in values[1:]:
            answer = ListNode(val, answer)
        return answer