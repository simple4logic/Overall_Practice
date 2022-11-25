from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('A')

        print(route[::-1])


a = Solution()

b1 = [["A", "B"], ["B", "E"], ["D", "E"], ["B", "D"], ["E", "B"]]
b2 = [["A", "B"], ["B", "F"], ["B", "X"], ["X", "B"]]
b3 = [["J", "S"], ["J", "A"], ["S", "A"], ["A", "J"], ["A", "S"]]

a.findItinerary(b2)


