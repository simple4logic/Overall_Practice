from typing import List
import re
import collections
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0 #max = -sys.maxsize
        min_val = prices[0] #min sys.maxsize

        for N in prices:
            min_val = min(min_val, N)
            max_price = max(max_price, N-min_val)

        return max_price

a = Solution()
s = [4, 6, 5, 8, 10, 5, 9, 3, 5, 12, 1, 10, 11, 7]
print(a.maxProfit(s))

#Output: [24,12,8,6]
        