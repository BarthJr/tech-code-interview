# Given a directed acyclic graph, with n vertices numbered from 0 to n-1,
# and an array edges where edges[i] = [from[i], to[i]] represents a directed edge from node from[i] to node to[i].
#
# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
#
# Notice that you can return the vertices in any order.

"""
>>> Solution().findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])
[0, 3]
>>> Solution().findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]])
[0, 2, 3]
"""
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = [False for _ in range(n)]

        for a, b in edges:
            nodes[b] = True

        return [i for i, node in enumerate(nodes) if not node]
