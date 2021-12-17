from typing import List
import re
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry: 
            #각 자릿수가 모두 더해질때까지! 만약 자릿수가 같고 carry in이 존재하면 한번 더 루프 돌려서
            #다음 자리까지 노드 하나 더 추가해줘야함. 즉 노드 개수 = 더 긴 리스트 길이 + 1

            #sum 매번 초기화
            sum = 0

            #두 리스트의 "자릿수"를 더함, 존재하는 경우에만 더함. 자릿수가 다른 수를 더할 수도 있음.
            if l1:
                sum+=l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next

            #divmod = A//10, A%10, 즉 10으로 나눈 몫과 나머지를 리턴
            carry, val = divmod(sum+carry, 10) #전 자리수에서 온 carry은 해봤자 1 or 0이다.
            head.next = ListNode(val)
            head = head.next

        return root.next
            


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