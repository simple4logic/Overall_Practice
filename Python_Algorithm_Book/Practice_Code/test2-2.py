from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #reversing linked-list
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev

    #divert linked-list to list
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next

        return list

    # List to linked-list
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    #add to linked-list with the functions above
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a) + int(''.join(str(e) for e in b)
        
        #return self.toReversedLinkedList(str(resultStr))

#to test, you have to make to linked-list manually. 
inp1 = [9,3]
inp2 = [4,5]
# inp1 = [1]
# inp2 = [3]

#list1_3 = ListNode(inp1[2], None)
list1_2 = ListNode(inp1[1], None)
list1 = ListNode(inp1[0], list1_2)

#list2_3 = ListNode(inp2[2], None)
list2_2 = ListNode(inp2[1], None)
list2 = ListNode(inp2[0], list2_2)

# list2 = ListNode(inp2[0], None)
# list1 = ListNode(inp1[0], None)

# list1 = ListNode(0, None)
# list2 = ListNode(0, None)

#for test
a = Solution()
#list1 = [1,2,4], list2 = [1,3,4]
head_node = a.addTwoNumbers(list1, list2)
while head_node:
    print(head_node.val)
    head_node = head_node.next