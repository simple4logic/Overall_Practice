from typing import List
import re
import collections

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s==s[::-1]: #filtering - single letter or whole palindrome
            return s



    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower()) #loop for pre-processing
        a: int = 1
        cnt: int = 0
        for element in arr: #swipe array to check [0] == [-1], next [1]==[-2], ···
            if element == arr[-a]:
                cnt+=1
                a+=1
        if cnt == len(arr):
            return true
        else:
            return false