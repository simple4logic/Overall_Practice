from typing import List
import re
import collections

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0 
        
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1] #한칸 밀어놨으니까 리턴할때는 한칸 앞에거 리턴
        
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None #포인터 둘이 겹치고 그 칸이 none

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None #포인터 둘이 겹치고 그 칸이 none이 아님