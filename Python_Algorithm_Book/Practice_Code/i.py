from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numdic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans: List = []
        size = len(digits)

        def dfs(size):
            tmp: str = ''
            


a = Solution()

a.letterCombinations("23")