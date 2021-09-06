# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
#
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat.
# The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3),
# and so on with the last couple being (2n - 2, 2n - 1).
#
# Return the minimum number of swaps so that every couple is sitting side by side.
# A swap consists of choosing any two people, then they stand up and switch seats.

"""
>>> Solution().minSwapsCouples([0,3,5,2,1,4])
2
>>> Solution().minSwapsCouples([0,2,1,3])
1
>>> Solution().minSwapsCouples([3,2,0,1])
0
>>> Solution().minSwapsCouples([1,4,0,5,8,7,6,3,2,9])
3
>>> Solution().minSwapsCouples([2,0,5,4,3,1])
1
"""

from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        for i in range(len(row)):
            row[i] = row[i] // 2

        graph = self.createGraph(row)
        visited = [False for _ in range(len(row) // 2)]
        swaps = 0

        for i in range(len(row) // 2):
            if not visited[i]:
                swaps += self.getClusterSize(graph, visited, i) - 1

        return swaps

    def getClusterSize(self, graph, visited, i):
        visited[i] = True
        swaps = 1

        for node in graph[i]:
            if not visited[node]:
                swaps += self.getClusterSize(graph, visited, node)

        return swaps

    def createGraph(self, row):
        graph = {}

        for i in range(len(row) // 2):
            graph[i] = set()

        for i in range(0, len(row), 2):
            person1 = row[i]
            person2 = row[i + 1]

            if person1 == person2:
                continue

            graph[person1].add(person2)
            graph[person2].add(person1)

        return graph
