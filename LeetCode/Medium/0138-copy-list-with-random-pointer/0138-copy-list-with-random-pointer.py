class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_dict = {}
        current_node = head
        # 반복문을 돌며 딕셔너리에 원래 노드를 키로하고, 새로 만든 노드를 value로 하여 넣는다.
        while current_node:
            node_dict[current_node] = Node(current_node.val)
            current_node = current_node.next
        current_node = head
        # 반복문을 돌며 새로 만든 노드의 next 노드와 random 노드를 설정한다.
        while current_node:
            node_dict[current_node].next = node_dict.get(current_node.next)
            node_dict[current_node].random = node_dict.get(current_node.random)
            current_node = current_node.next
        return node_dict[head]