class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values_left = []
        values_mid = []
        values_right = []
        index = 1
        # left 이전 노드는 values_left, 중간은 mid, right 이후 노드는 right에 넣는다.
        while head:
            if index < left:
                values_left.append(head.val)
            elif index > right:
                values_right.append(head.val)
            else:
                values_mid.append(head.val)
            head = head.next
            index += 1
        # 링크드 리스트를 만들기위해 거꾸로 배열을 이어 붙힘
        values = values_right[::-1] + values_mid + values_left[::-1]
        # 마지막 노드부터 연결
        answer = ListNode(values[0], None)
        for val in values[1:]:
            answer = ListNode(val, answer)
        return answer