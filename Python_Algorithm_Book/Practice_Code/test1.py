from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sero = len(grid)
        garo = len(grid[0])
        discovered = [] #탐색 완료된 그리드 상의 좌표
        nums = 0
    
        for i in range(sero): #세로 길이
            for j in range(garo): #가로 길이
                if grid[i][j] == "0" or (i,j) in discovered:
                    continue
                else: 
                    iteration(i,j)
                    nums += 1
        return nums


def recursive(i: int, j: int):
    discovered.append((i,j))
        for tuples in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if tuples[0] >= sero or tuples[0] < 0 or tuples[1] >= garo or tuples[1] < 0:
                continue
            if grid[tuples[0]][tuples[1]] == "0":
                continue
            self.recursive(tuples)
    return