from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            a: str = s[i] #save first
            print(a)
            s[i]=s[-(i+1)]
            print(s[i])
            s[-(i+1)] = a
        print(s)

s = Solution()
s.reverseString(["a","b","c","d"])
