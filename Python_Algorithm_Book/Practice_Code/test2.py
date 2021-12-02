from typing import List
import re
import collections

# three sum is zero
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        if not nums:
            return []
        
        for i in range(len(nums)-2): #'cause next two elements i, i+1, i+2
            if i>0 and nums[i]==nums[i-1]: #when current value is same as the previous one, skip it!
                continue
            left, right = i+1, len(nums) - 1
            
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1 #even if left +=1 but same situation, repeat it
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1                    
                    right -= 1
                    left += 1
        return ans



ans = Solution()
nums = [-1,0,1,2,-1,-4]
#nums = [0]
pt = ans.threeSum(nums)
print(pt)
