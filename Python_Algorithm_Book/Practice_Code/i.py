from typing import List
import re
import collections

class MyStack:

    def __init__(self):
        #def with the type deque
        stack = collections.deque()

    def push(self, x: int) -> None:
        stack.append(x)

    def pop(self) -> int:
        return stack.pop()

    def top(self) -> int:
        top = stack.pop()
        stack.append(top)
        return top         

    def empty(self) -> bool:
        if self:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()