from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if(not l1) or (l2 and l1.val > l2.val): # l1이 none일 때// 또는 // l2가 존재하고, l1이 l2보다 클 때 실행.
            l1, l2 = l2, l1
        if l1: #교체한 뒤에 l1이 존재하면, 다음 주소를  l1으로 할당 <- 이전 아웃풋인 l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

#to test, you have to make to linked-list manually. 
inp1 = [-9,3]
inp2 = [4,5]

list1_2 = ListNode(inp1[1], None)
list1 = ListNode(inp1[0], list1_2)

list2_2 = ListNode(inp2[1], None)
list2 = ListNode(inp2[0], list2_2)

#for test
a = Solution()
a.mergeTwoLists(list1, list2)