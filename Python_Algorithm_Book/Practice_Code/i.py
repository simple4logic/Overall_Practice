from typing import List
import re

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def recursive(i: int, j: int, discovered_list=[]):
        discovered_list.append((i, j))
        for tuples in [(i+1, j), (i, j+1)]:
            if tuples not in discovered_list:
                discovered_list = recursive(*tuples, discovered_list)
        return discovered_list


    return ans
    
    

            


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(grid[])

a= Solution()
Ans = a.numIslands(grid)
print(Ans)