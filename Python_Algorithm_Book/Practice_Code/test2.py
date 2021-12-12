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
        node = ListNode()

        while l1.next or l2.next: #until both are the false
        #for i in range(30):
            if (l1.val >= l2.val) or (not l1.next): #l1이 끝자락이면 이제 l2를 민다.
                node = l2
                print(node.val, "appended value of l2")
                node = node.next
                if(l2.next):
                    l2 = l2.next
            else:
                node = l1
                print(node.val, "appended value of l1")
                node = node.next
                if(l1.next):
                    l1 = l1.next                

        while head:
            print(head.val, "start printing")
            head = head.next




'''
왠지 node를 하나씩 밀견서 그 value를 비교 시키고 작은쪽을 append 하면 될 것 같다.

1 4 6
1 5 7
이렇게 있으면 리스트1의 1넣고(>=) 한칸밀고
4와 1 비교시킨다음 리스트2의 1넣고 한칸밀고 이런식으로...


'''

#to test, you have to make to linked-list manually. 
inp1 = [1,2,3]
inp2 = [4,5,6]
list1_3 = ListNode(inp1[2], None)
list1_2 = ListNode(inp1[1], list1_3)
list1 = ListNode(inp1[0], list1_2)

list2_3 = ListNode(inp2[2], None)
list2_2 = ListNode(inp2[1], list2_3)
list2 = ListNode(inp2[0], list2_2)

#for test
a = Solution()
#list1 = [1,2,4], list2 = [1,3,4]
a.mergeTwoLists(list1, list2)