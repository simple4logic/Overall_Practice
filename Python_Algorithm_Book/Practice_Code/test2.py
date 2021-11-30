from typing import List
import re
import collections

# three sum is zero
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twotarget(left :int, right :int, target : int) -> str:
            while not left==right:
                if nums[left]+nums[right] < target:
                    left += 1
                else:
                    right -= 1

        for i in nums:
            
