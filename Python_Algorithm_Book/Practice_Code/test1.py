from typing import List

'''
메모 1. 파이썬에서 tmplist = A(which type is list) 처럼 할당할 경우 아예 A 리스트에 대한 참조가 추가되기 때문에 tmplist에서
수정이 가해질 경우 A에서도 실제로 수정이 가해진다. 따라서 tmplist = A[:] 처럼 해야지 그냥 list의 모든 element들이 복사되게 된다.
이 점을 꼭 주의할 것!! 
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        Ans: List[List[int]] = []

        def minus(list, int):
            templist = list[:]
            templist.remove(int)
            return templist

        # currentlist = 내가 현재 쌓아나가고 있는 list, leftlist = 빠져나가고 있는 list
        def recursion(_leftlist: List, _currentlist: List):
            # 직접 참조를 막기 위해 복사만 함
            leftlist = _leftlist[:]
            currentlist = _currentlist[:]

            if(len(leftlist) == 0):
                print("ans appended")
                Ans.append(currentlist)
                return

            for N in leftlist:
                print("this is N", N)
                print("left list before this loop", leftlist)
                recursion(minus(leftlist,N), currentlist+[N])
            
        if(nums):
            recursion(nums, [])

        print(Ans)
        return Ans


        


a = Solution()

b = [1, 2, 3]

a.permute(b)