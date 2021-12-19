from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        #definition of the rev function
        def rev(head: ListNode, length: int)-> ListNode, ListNode:
            rev = None
            node = head
            for i in range(length-1):
                rev, rev.next, node = node, rev, node.next
            last_add = node.next
            rev, rev.next = node, rev
            return rev, last_add
        
        #filtering single node-list
        if not head.next:
            return head
        
        #saving head node
        head_node = head

        for i in range(left-2):
            head = head.next

        head.next, lastadd = rev(head.next, right-left+1)

        while          


inp1= [1,2,3,4,5,6,7,8,9]
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
head_node = a.reverseBetween(link1)
while head_node:
    print(head_node.val)
    head_node = head_node.next