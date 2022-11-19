from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numdic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans: List = []
        fullsize = len(digits)

        def dfs(size: int, tmp: str):
            if size <= 1:
                ans.append(tmp)
                return

            for B in numdic[digits[fullsize - size + 1]]:
                dfs(size-1, tmp+B)
            

        
        if(digits):
            for A in numdic[digits[0]]:
                tmp: str = ''
                dfs(fullsize, tmp+A)

        return ans



a = Solution()

a.letterCombinations("222")