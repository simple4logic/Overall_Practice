from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        if not node or not node.next: #when (0 or 1 node)
           return node
        
        head_node = ListNode(0, node.next) #point second node
        prev = ListNode()

        while node and node.next: #노드가 하나면,첨부터 false이므로 루프 통과X
            prev.next = node.next
            temp = node
            node = node.next
            temp.next = node.next
            node.next = temp
            prev = temp
            print(node.val, temp.val)
            node = node.next.next
        
        return head_node.next
            


#to test, you have to make to linked-list manually. 
inp1= [1,2,3,4, 5,6,7,8,9]
def makeLinkedList(inp: List) -> ListNode:
    node = ListNode()
    head = node
    for val in inp:
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
        node = node.next
    return head

link1 = makeLinkedList(inp1).next

#for test
a = Solution()
head_node = a.swapPairs(link1)
while head_node:
    print(head_node.val)
    head_node = head_node.next