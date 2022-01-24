from typing import List
import re
import collections
import heapq

class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        #init size = 1000, if over 1000 get same key(using individual chaining)
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        #No Node -> append then exit.
        if self.table[index].value is None:
            self.table[index] = Node(key, value)
            return
        
        #When Key exist, build up the duplicated values with linked-list.
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = Node(key, value)


    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        while p:
            if p.key == key:
                self.table[index] = Node() if p.next is None else p.next
                return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# Your MyHashMap object will be instantiated and called as such:
a = MyHashMap()
#obj.put(key,value)
a.put(1, 'a')
a.put(2, 'f')
a.put(3, 'd')
a.put(6, 'g')
print(a.l)
print(a.get(3))
a.remove(3)
print(a.get(3))
print(a.l)
a.put(1, 'x')
print(a.l)
#obj.remove(key)
