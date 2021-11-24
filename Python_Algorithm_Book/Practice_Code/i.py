from typing import List
import re
import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                        return [i, j]

#for testing
a = Solution()
nums = [3, 2, 4]
target = 6
print(a.twoSum(nums, target))
