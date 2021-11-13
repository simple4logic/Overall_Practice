#Q1 Valid Palindrome

'''
pre-processing by filtering input.
isalnum() is the method that checks whether object is (number or english) or not.
'''

'''
#this is the pre-processing function that made input regular lower-case english(or number).
arr = []
for char in arr:
    if char.isalnum(): #to check input 'char' is num&Eng or not, if true, return true. Vice versa.
        arr.append(char.lower()) #if true, append it to the list.
'''

#1. my solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        a: int = 1
        cnt: int = 0

        for element in arr:
            if element == arr[-a]:
                cnt+=1
                a+=1

        if cnt == len(arr):
            return true
        else:
            return false
        
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")

