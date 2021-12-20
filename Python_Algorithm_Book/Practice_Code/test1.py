from typing import List
import re
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            #전체 집합과 접미사 집합이 일치할 경우 분리한다
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters()
        return ''
        

a = Solution()
s = "cbacdcbc"
print(a.removeDuplicateLetters(s))
