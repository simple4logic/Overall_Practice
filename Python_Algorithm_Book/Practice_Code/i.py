from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        # print(graph)
        
        def dfs(startfrom: str, path):
            if ans:
                return
            # print("this is ans", path)
            # print("this is graph", graph)

            if len(path) > len(tickets):
                print("ans returned", path)
                ans.append(path)
                return

            # print("graph(startfrom) is", graph[startfrom])
            for N in graph[startfrom]:
                # print("this is turn of N = ", N)
                graph[startfrom].remove(N)
                dfs(N, path+[N])
                # print("after path", path)
                graph[startfrom].insert(0, N)

        start = "A"
        dfs(start, [start])
        # print(ans)
        return ans[0]


a = Solution()

b1 = [["A", "B"], ["B", "E"], ["D", "E"], ["B", "D"], ["E", "B"]]
b2 = [["A", "B"], ["B", "F"], ["B", "X"], ["X", "B"]]
b3 = [["J", "S"], ["J", "A"], ["S", "A"], ["A", "J"], ["A", "S"]]

a.findItinerary(b2)


