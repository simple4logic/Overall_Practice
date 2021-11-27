from typing import List
import re
import collections

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #check if the list is empty or not
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1 #each first & last idx
        left_max, right_max = height[left], height[right] #initial value is both edge(right & left).

        while left < right: #while two-pointer meets
            left_max, right_max = max(height[left], left_max),\
                                  max(height[right], right_max) #compare previous value against current value
            
            if left_max <= right_max: #until both right & left max column converges to the highest column
                volume+= left_max - height[left]
                left+=1
            else:
                volume+= right_max - height[right]
                right-=1
            
        return volume
   
#for testing
a = Solution()
s = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(s))