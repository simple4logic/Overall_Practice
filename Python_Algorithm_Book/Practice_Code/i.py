from typing import List
import re
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        #insert to heap as negative

        for f in freqs:
            #f is the key, freqs[f] is the value(frequency)
            #insert it SWAPPED
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()

        for _ in range(k):
            #pop out k-times
            #min-heap, so pop from the smallest value
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
        
a = Solution()
s = [1,1,2,2,2,2,3,5,5,5]
ans = a.topKFrequent(s,2)
print(ans)

'''
1111 222 33

1: 4개 , 2 : 3개, 3: 2개
1, 2, 3 (key)
개수(value)

상위 k번!!
'''