from typing import List
import re
import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        #keys ) } ], values ( { [
        table = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char not in table: #table "keys"
                stack.append(char)

            #if only once wrong, return false & if stack is empty
            # when close parantheses appears first, IN TABLE but STACK IS EMPTY
            elif not stack or stack.pop() != table[char]:
                return False 

        return len(stack) == 0 #check if the stack is empty

a = Solution()
if a.isValid("()"):
    print("True")
else:
    print("False")