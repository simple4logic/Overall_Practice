from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        l1, l2 = list1, list2
        head = None

        #filter of empty cases
        if not l1 and not l2: #둘다 empty인 경우
            return head
        if not l1: #l1가 empty인 경우
            return l2
        if not l2:
            return l1

        #start, init. Declare which to start
        if (l1.val >= l2.val):
            head = l2
            head_node = head
            l2 = l2.next
            if(not l2): #filter of one letter case
                head.next = l1
                return head_node
        else:
            head = l1
            head_node = head
            l1 = l1.next
            if(not l1): #filter of one letter case
                head.next = l2
                return head_node
        
        #head_node = head
                
        while l1 or l2: #until both are the false
            if (l1.val >= l2.val):
                head.next = l2
                head = head.next
                l2 = l2.next
                if(not l2): #l2가 none이면 실행됨
                    head.next = l1
                    return head_node

            else:
                head.next = l1
                head = head.next
                l1 = l1.next
                if(not l1): #l1가 none이면 실행됨
                    head.next = l2
                    return head_node

        return head_node


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
a.mergeTwoLists(list1, list2)