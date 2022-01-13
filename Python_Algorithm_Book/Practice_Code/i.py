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
        self.dq = Node()
        self.head = self.dq
        self.tail = self.dq
        self.maxlen = k
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        

    def insertLast(self, value: int) -> bool:
        

    def deleteFront(self) -> bool:
        

    def deleteLast(self) -> bool:
        

    def getFront(self) -> int:
        

    def getRear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        

