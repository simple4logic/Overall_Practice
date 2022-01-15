from typing import List
import re
import collections

class Node():
    def __init__(self, val = None, prev = None, next = None): #값, 전 주소, 다음 주소
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.maxlen = k
        self.cnt = 0

    def _add(self, node: Node(), new_node: Node()):
        a = node.next
        node.next = new_node
        new_node.prev, new_node.next = node, a
        a.prev = new_node

    def _del(self, node: Node()):
        prev, next = node.prev, node.next
        node.next.prev = prev
        node.prev.next = next

    def insertFront(self, value: int) -> bool:
        if self.cnt == self.maxlen:
            return False
        else:
            self.cnt += 1
            self._add(self.head,Node(value))
            return True

    def insertLast(self, value: int) -> bool:
        if self.cnt == self.maxlen:
            return False
        else:
            self.cnt += 1
            self._add(self.tail.prev, Node(value))
            return True

    def deleteFront(self) -> bool:
        if self.cnt == 0:
            return False
        else:
            self.cnt -= 1
            self._del(self.head.next)
            return True

    def deleteLast(self) -> bool:
        if self.cnt == 0:
            return False
        else:
            self.cnt -= 1
            self._del(self.tail.prev)
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.cnt == 0:
            return True
        else:
            return False        

    def isFull(self) -> bool:
        if self.cnt == self.maxlen:
            return True
        else:
            return False
