from typing import List
import re
from collections import Counter

class Solution:
    def stringsort(self, strs: str) -> str:
        la = sorted(strs)
        return "".join(la)   

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for words in strs:
            dic[words] = stringsort(words) #word : sorted word
        print(dic)



#for testing
a = Solution()
s = ["eat","tea","tan","ate","nat","bat"]
a.groupAnagrams(s)