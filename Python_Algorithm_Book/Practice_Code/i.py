from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True #to prevent the event that input is 0 node. "But" in this Q, node count can not be zero

        ansl :list = []

        node = head

        while node is not None:
            ansl.append(node.val)
            node = node.next

        while len(ansl)>1: #if len = 1, stop. Actually single letter left so true.// if len = 0, stop.
            if ansl.pop(0) != ansl.pop():
                return False
        
        return True

#to test, you have to make to linked-list manually. 
inp = [1,2,2,1] #inp = input as head
node3 = ListNode(inp[3])
node2 = ListNode(inp[2], node3)
node1 = ListNode(inp[1], node2)
head = ListNode(inp[0], node1)


#for test
a = Solution()
a.isPalindrome(head)


