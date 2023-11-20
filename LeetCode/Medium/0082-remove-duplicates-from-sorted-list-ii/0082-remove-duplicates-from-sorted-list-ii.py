# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 현재 보고있는 노드, 중복되지 않은 노드의 tail, 중복되지 않은 노드의 head
        temp, tail, answer = head, None, None
        # 현재 보고 있는 노드가 중복되는 노드인지
        is_duplicate = False
        # 전체 노드 순회
        while temp:
            next_node = temp.next
            # 다음 노드와 값이 다르고, 중복되지 않았으면 tail을 갱신
            if not next_node or temp.val != next_node.val:
                if not is_duplicate:
                    if not tail:
                        tail = temp
                        answer = temp
                    else:
                        tail.next = temp
                        tail = temp
                if next_node:
                    is_duplicate = False
            else:
                is_duplicate = True
            temp = next_node
        # tail뒤의 노드들이 중복되었으면 삭제
        if is_duplicate and tail:
            tail.next = None
        return answer