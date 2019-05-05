# Given a 2d grid map of '1's (land) and '0's (water),
# count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

"""
>>> grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
>>> num_islands(grid)
1
>>> grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
>>> num_islands(grid)
3

>>> grid = [['0', '0', '0', '0', '0']]
>>> num_islands(grid)
0
>>> grid = []
>>> num_islands(grid)
0

"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    num_islands = 0

    if not grid:
        return num_islands

    lin_len = len(grid)
    col_len = len(grid[0])

    def dfs(i, j):
        if 0 <= i < lin_len and 0 <= j < col_len and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(dfs, (i - 1, i + 1, i, i), (j, j, j - 1, j + 1)))

    for i in range(lin_len):
        for j in range(col_len):
            if grid[i][j] == '1':
                dfs(i, j)
                num_islands += 1
    return num_islands
