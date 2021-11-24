from typing import List
import re
import collections

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s)-1 and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        result = ''
        for i in range(len(s)):
            result = max(result,
                        expand(i, i+1),
                        expand(i,i+2),
                        key=len)
        return result

        if s==s[::-1]:
            return s

a = Solution()
s = "babad"
print(a.longestPalindrome(s))