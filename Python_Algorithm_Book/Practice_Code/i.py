from typing import List
import re
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=collections.defaultdict(list)
        #dic={}

        for words in strs:
            dic[''.join(sorted(words))].append(words)
        print(list(dic.values()))

#for testing
a = Solution()
s = ["eat","tea","tan","ate","nat","bat"]
a.groupAnagrams(s)