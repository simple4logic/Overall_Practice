from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode) -> bool:
        node = head
        rev = None

        while node: #until node has value
            rev, rev.next, node = node, rev, node.next
        
        while rev:
            print(rev.val)
            rev = rev.next
'''
rev <- slow //in first loop, rev is the head
rev.next <- rev //in first loop, 
slow <- slow.next

'''

#to test, you have to make to linked-list manually. 
inp = [1,2,3,4] #inp = input as head
node3 = ListNode(inp[3])
node2 = ListNode(inp[2], node3)
node1 = ListNode(inp[1], node2)
head = ListNode(inp[0], node1)


#for test
a = Solution()
a.reverse(head)