from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = paragraph.lower()
        a = re.sub('[\W]',' ',a) #특수문자들 모두 space로 변경
        lis = a.split() # split by space
        cntdic = Counter(lis)
        t = banned[0]
        if t in cntdic:
            del cntdic[t]
        #print(max(cntdic.keys()))

a = Solution()
s = "Bob hit a ball, the hit BALL flew far after it was hit."
a.mostCommonWord(s, ["hit"])