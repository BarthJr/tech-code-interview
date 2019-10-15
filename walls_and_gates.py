# https://www.lintcode.com/problem/walls-and-gates/description

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = INF to represent INF as you may assume that
# the distance to a gate is less than INF.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a ROOM, that room should remain filled with INF

"""
>>> INF = 2147483647
>>> grid = [
...          [INF, -1, 0, INF],
...          [INF, INF, INF, -1],
...          [INF, -1, INF, -1],
...          [0, -1, INF, INF]
...        ]
>>> Solution().wallsAndGates(grid)
>>> grid
[[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
"""


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    GATE = 0

    def wallsAndGates(self, rooms):
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == self.GATE:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, distance):
        if self.out_of_bounds(rooms, i, j):
            return
        elif rooms[i][j] < distance:
            return

        rooms[i][j] = distance
        self.traverse(rooms, i, j, distance)

    def out_of_bounds(self, rooms, i, j):
        return i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0])

    def traverse(self, rooms, i, j, distance):
        self.dfs(rooms, i + 1, j, distance + 1)
        self.dfs(rooms, i - 1, j, distance + 1)
        self.dfs(rooms, i, j + 1, distance + 1)
        self.dfs(rooms, i, j - 1, distance + 1)
