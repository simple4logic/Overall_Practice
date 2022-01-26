from typing import List
import re
import collections

from typing import List
import re
import collections
import heapq

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        cnt = 0

        #substitute counter module
        for a in list(stones):
            if a not in freq:
                freq[a] = 1 #append new one
            else:
                freq[a] += 1

        for b in list(jewels):
            num = freq[b]
            if num != 0:
                cnt += num

        return cnt


# word = input()
# print(word)
# counter = collections.Counter(word)
# print(counter)
# print(counter['x'])

a = Solution()
J = "aA"
S = "aAAbbbb"
A = a.numJewelsInStones(J, S)
print(A)


