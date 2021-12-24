from typing import List
import re
import collections

class MyStack:

    def __init__(self):
        #def with the type deque
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.q.reverse()
        pop = self.q.popleft()
        self.q.reverse()
        return pop

    def top(self) -> int:
        self.q.reverse()
        top = self.q.popleft()
        self.q.reverse()
        self.q.append(top)
        return top         

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(9)
obj.push(8)
param_2 = obj.pop()
print(obj.q)
param_3 = obj.top()
print(obj.q)
param_4 = obj.empty()
print(param_4, obj.q)
