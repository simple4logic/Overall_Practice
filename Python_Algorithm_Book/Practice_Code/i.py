from typing import List
import re
import collections

# 첫 1에서 시작하는건 잘 모르겠고 중간부터 일단 구현해봄

def dfs(start_point :(int, int)):
    stack = [start_point]
    discovered = []
    near = []

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            #여기서 v 상, 하, 좌, 우 순으로 탐색해서 1인 좌표만 찾아서 임시 리스트 near에 저장해두셈
            for tuples in near:
                stack.append(tuples)

    # 그다음 뭘 리턴해야할지는 잘 몰루? 아마 한번 섬 모두다 탐색 완료했으면 전역변수에 +1 리턴하고
    # 다음 탐색 들어가기 ㄱㄱ 다음에는 not discovered인 동시에 1인 point를 인수로 넣어서 확인하면 되겠네