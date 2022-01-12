from typing import List
import re
import collections

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0 #front pointer
        self.rear = -1 #rear pointer #첫 삽입 때 뒤로 한 칸 밀림
        self.cnt = 0
        
    def enQueue(self, value: int) -> bool: #삽입이 이루어질때는 rear만 이동한다
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1)%(self.maxlen) #rear를 뒤로 한칸 민다
            self.q[self.rear] = value
            self.cnt += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1)%(self.maxlen) #front를 뒤로 한칸 민다
            self.cnt -= 1
            return True

    def Front(self) -> int:
        a = self.q[self.front]
        if a == None:
            return -1
        else:
            return a

    def Rear(self) -> int:
        b = self.q[self.rear]
        if b == None:
            return -1
        else:
            return b
        
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
        


# Your MyStack object will be instantiated and called as such:
obj = MyCircularQueue(8)
p1 = obj.enQueue(3)
print(p1, obj.front,obj.rear)
p2 = obj.enQueue(9)
print(p2, obj.front,obj.rear)
p3 = obj.enQueue(5)
print(p3, obj.front,obj.rear)
p4 = obj.enQueue(0)
print(p4, obj.front,obj.rear)
p5 = obj.deQueue()
print(p5, obj.front,obj.rear)
p6 = obj.deQueue()
print(p6, obj.front,obj.rear)
p7 = obj.Rear()
print(p7)
#print(obj.q)

#print(obj.isFull())
