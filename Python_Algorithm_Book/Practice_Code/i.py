from typing import List
import re
import collections
import heapq

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewlist, stlist = [jewels.split()], [stones.split()]
        counter = collections.Counter(stlist) #key : value, key가 알파벳, value가 개수
        ans = 0

        for x in jewlist:
            if counter[x]
