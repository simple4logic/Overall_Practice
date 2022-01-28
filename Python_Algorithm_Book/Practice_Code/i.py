from typing import List
import re
import collections
import heapq

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def expand(left: int, right : int) -> str:
            temp = set()
            
            while left>=0 and right<len(s) and (s[left] not in temp) and (s[right] not in temp):
                if (right != left) and (s[right] == s[left]):
                    break
                temp.add(s[left])
                temp.add(s[right])
                left -= 1
                right +=1  
            #print("before exit", temp)
            #print("this is length", len(s[left + 1:right]))
            return s[left + 1:right]

        result = ''
        for i in range(len(s)):
            #print("loop", i)
            result = max(result, expand(i, i+1), expand(i, i), key=len) #i, i+1 -> 짝수 case // i,i -> 홀수 case

        return len(result)


a = Solution()
# s = "abcabcbb"
s = 'a'
ans = a.lengthOfLongestSubstring(s)
print(ans)


'''
sliding window로 풀어보기
1칸으로 시작해서 양옆으로 2칸씩 확장
2칸으로 시작해서 양옆으로 2칸씩 확장
중복이 검출 될 시에 현재 maxlen에 저장하고 
다음 loop(start point)로 넘어가기
'''
