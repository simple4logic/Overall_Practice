from typing import List
import re
import collections

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) ->str:
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            #when escaped from the while loop, this array has much more index than palindrome.
            #ZXXXXY condition or XXXXY (left is - index) or ZXXXX (right exceeds the length)
            #therefore returns the index "left+1", and "right"(in string slicing, :right returns until right-1 index)
            return s[left+1:right]

        if len(s) < 2 or s==s[::-1]: #filtering - single letter or whole palindrome
            return s

        result = '' #gen blank string
        for i in range(len(s)-1):
            result = max(result,
                            expand(i, i+1), #abbc : even number two pointer
                            expand(i, i+2), #axyxc : odd number two pointer
                            key=len #the criteria for checking max is length of string
                            )
        return result

a = Solution()
s = "babad"
print(a.longestPalindrome(s))
