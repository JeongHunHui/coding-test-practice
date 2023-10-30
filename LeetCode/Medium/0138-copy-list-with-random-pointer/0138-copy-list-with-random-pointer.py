class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeDict = {}
        currentNode = head
        while currentNode:
            nodeDict[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next
        currentNode = head
        while currentNode:
            nodeDict[currentNode].next = nodeDict.get(currentNode.next)
            nodeDict[currentNode].random = nodeDict.get(currentNode.random)
            currentNode = currentNode.next
        return nodeDict[head]