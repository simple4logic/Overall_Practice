from typing import List
import re
import collections

# t is between 30 ~ 70
# T.index(element) returns index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        ans, stack = [0 for i in range(len(T))], [] #init ans with 0

        for val in T:
            cur_idx = T.index(val)
            
            if not stack: #스택에 없다면 append / 첫번째 원소 filetering
                stack.append(val)
                continue
            
            while stack and stack[-1] < val: #stack이 있고, 마지막 값보다 지금 값이 더 크면 반복
                last_idx = T.index(stack.pop())
                stack.append(val)
                ans[last_idx] = cur_idx - last_idx

            print(stack, ans, cur_idx)

        return ans  
        
        

a = Solution()
t = [73,74,75,71,69,72,76,73]
print(a.dailyTemperatures(t))
