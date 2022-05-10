class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        discovered = [] #탐색 완료된 그리드 상의 좌표
        nums = 0

        def recursive(i: int, j: int):
            discovered.append((i, j))
            for tuples in [(i+1, j), (i, j+1)]:
                if tuples not in discovered:
                    discovered = recursive(*tuples, discovered)
            return discovered

        for i in range(grid.length): #세로 길이
            for j in range(grid[i].length): #가로 길이
                if grid[i][j] == 0:
                    continue
                else:
                    if (i,j) in discovered:
                        continue
                    else:
                        recursive(i,j)
                        nums += 1
    return nums
    




'''
grid만 given. grid는 grid[i][j] 형태로 element에 접근 가능

recursive루프의 역할 = 연결된 육지 좌표에 싹다 discovered를 마킹
루프에서 나오는 순간 그건 이미 섬 하나임

따라서 루프를 몇번 반복하냐에 따라서 섬의 개수를 알 수 있다



'''
    
