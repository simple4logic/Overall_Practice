from typing import List
import re
import collections
import heapq

class Node():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def mergeLists(self, lists: List[Node]) -> Node:
        root = result = Node(None) #save result's address at root
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                headq.headpush(heap, (lists[i].val), i, lists[i])
        
        while heap:
            node = headq.headpop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                headq.headpush(heap, (result.next.val, idx, result.next))

        return root.next
