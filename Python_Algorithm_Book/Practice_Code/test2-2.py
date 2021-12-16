from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##연결 리스트별로 최소 하나 이상의 원소를 가짐

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1, ls2 = [], [] #define empty list
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        #finish conversion to the list
        


#to test, you have to make to linked-list manually. 
inp1 = [-9,3]
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

#for test
a = Solution()
#list1 = [1,2,4], list2 = [1,3,4]
a.addTwoNumbers(list1, list2)