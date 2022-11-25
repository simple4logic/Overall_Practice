from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


a = Solution()

b1 = [["A", "B"], ["B", "E"], ["D", "E"], ["B", "D"], ["E", "B"]]
b2 = [["A", "B"], ["B", "F"], ["B", "X"], ["X", "B"]]
b3 = [["J", "S"], ["J", "A"], ["S", "A"], ["A", "J"], ["A", "S"]]

a.findItinerary(b2)


