from typing import List
import re
import collections

# t is between 30 ~ 70
# T.index(element) returns index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        ans, stack = [0] * len(T), [] #init ans with 0

        for i, val in enumerate(T):
    
            while stack and T[stack[-1]] < val: #stack이 있고, 마지막 값보다 지금 값이 더 크면 반복
                last_idx = stack.pop()
                ans[last_idx] = i - last_idx

            # index itself is stacked!!
            stack.append(i)

        return ans  
        
'''
문제점 = T.index(stack.pop())에서 만약 pop한 값이 동일하다면 index를 어디서 찾는가?
>> sol : stack을 index로 해결!!
'''

a = Solution()
t = [89,62,70,58,47,47,46,76,100,70]
print(a.dailyTemperatures(t))

#ans [8,1,5,4,3,"2",1,1,0,0]
