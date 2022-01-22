from typing import List
import re
import collections
import heapq

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.l = []
        

    def put(self, key: int, value: int) -> None:
        New_Node = Node(key, value)
        self.l.append(New_Node)        

    def get(self, key: int) -> int:
        #if key in [x.key for x in self.l]: #when 1 is in [(1, a), (2, c), (3, f), (4, b), (5, r)]
        for nodes in self.l:
            if

        else:
            return -1
        

    def remove(self, key: int) -> None:
        


# Your MyHashMap object will be instantiated and called as such:
a = MyHashMap()
#obj.put(key,value)
a.put(1, 1)
print(a)
#param_2 = obj.get(key)
#obj.remove(key)
