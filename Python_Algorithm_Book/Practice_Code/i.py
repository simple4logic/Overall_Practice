from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head #the list to reverse
        rev = None # the space that reversed list is saved
        while node:
            rev, rev.next, node = node, rev, node.next
        return rev

#to test, you have to make to linked-list manually. 
inp = [1, 3, 5, 9]

list4 = ListNode(inp[3], None)
list3 = ListNode(inp[2], list4)
list2 = ListNode(inp[1], list3)
list1 = ListNode(inp[0], list2)

#for test
a = Solution()
new_head = a.reverseList(list1)

while new_head:
    print(new_head.val)