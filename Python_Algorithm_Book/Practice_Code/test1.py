from typing import List
import re
import collections

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self) -> bool:
        return self.input == [] and self.output == []


obj = MyQueue()
obj.push(1)
print(obj.q)
obj.push(2)
print(obj.q)
print(obj.peek())
print(obj.q)
obj.pop()
print(obj.q)
print(obj.empty())