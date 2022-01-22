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
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        

    def get(self, key: int) -> int:
        for x in self.l: #x = [1, a]
            if x[0] == key:
                return x[1]
        return -1
        

    def remove(self, key: int) -> None:
        for x in self.l: #x = [1, a]
            if x[0] == key:
                self.l.remove(x)
                return
        return
        


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
