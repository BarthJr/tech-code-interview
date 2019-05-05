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


def find_lands(grid, visited):
    lands = set()
    lin_len = len(grid)
    col_len = len(grid[0])
    for i in range(lin_len):
        for j in range(col_len):
            if grid[i][j] == '1' and (i, j) not in visited:
                lands.add((i, j))
    return lands


def adjacents(grid, position):
    i, j = position

    line_length = len(grid)
    col_length = len(grid[0])
    res = [
        (max(i - 1, 0), j),
        (min(i + 1, line_length - 1), j),
        (i, max(j - 1, 0)),
        (i, min(j + 1, col_length - 1))]
    return res


def num_islands(grid: List[List[str]]) -> int:
    num_islands = 0
    if not grid:
        return num_islands
    visited = set()
    lands = find_lands(grid, visited)
    if not lands:
        return num_islands
    to_be_visited = set([lands.pop()])
    if None in to_be_visited:
        return num_islands
    while to_be_visited:
        has_parent_land = False
        while to_be_visited:
            current_position = to_be_visited.pop()
            visited.add(current_position)
            has_parent_land = True

            for p in adjacents(grid, current_position):
                lin, col = p
                if (grid[lin][col] == '1') and (p not in visited):
                    to_be_visited.add(p)
                    if p in lands:
                        lands.remove(p)

        if has_parent_land:
            num_islands += 1

        if not lands:
            return num_islands
        to_be_visited = set([lands.pop()])
        if None in to_be_visited:
            return num_islands

    return num_islands
