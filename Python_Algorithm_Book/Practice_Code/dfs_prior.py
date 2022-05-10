#dfs 하위 함수를 테스트 하기 위한 파일
from typing import List

discovered = []

def iteration(i: int, j: int):
    stack = [(i, j)]
    while stack:
        v = stack.pop()
        print(v)
        if v not in discovered:
            discovered.append(v)
            for tuples in [(v[0], v[1]+1), (v[0]+1, v[1])]:
                stack.append(tuples)
    return discovered

iteration(0,0)

'''
문제점
2d 그리드에 최대치가 없어서 무한루프가 생김
최대치를 어떻게 넣을 것인가?
'''