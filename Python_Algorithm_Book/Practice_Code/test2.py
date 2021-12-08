#Q561 Array Partition I
# 12/06 start p190 in the book

from typing import List
import re
import collections

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        tmp1=[1 for i in range(len(nums))]
        tmp2=[1 for j in range(len(nums))]

        for i in range(len(nums)):
            if i == 0: #for i-1 index
                continue
            tmp1[i] = tmp1[i-1] * nums[i-1]
            
        for j in range(len(nums)):
            if j == 0: #for i-1 index
                continue
            tmp2[j] = tmp2[j-1] * nums[-1-(j-1)]

        tmp3 = list(map(lambda x,y : x*y,tmp1, reversed(tmp2)))
        return tmp3

a = Solution()
nums = [1,2,3,4]
print(a.productExceptSelf(nums))

#Output: [24,12,8,6]
        