# You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
# Each 0 represents land, and each 1 represents part of a river.
# A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent)
# The number of adjacent 1s forming a river determine its size.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix.
# Note that these sizes do not need to be in any particular order.


RIVER = 1


def river_sizes(matrix):
    seen = set()
    queue = []
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == RIVER and (i, j) not in seen:
                traverse_node(i, j, matrix, queue, result, seen)
    return result


def get_valid_paths(position, matrix, seen):
    valid_paths = []
    paths = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for path in paths:
        x = position[0] + path[0]
        y = position[1] + path[1]
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == RIVER and (x, y) not in seen:
            valid_paths.append((x, y))
    return valid_paths


def traverse_node(i, j, matrix, queue, result, seen):
    queue.append((i, j))
    river_size = 0
    while queue:
        next = queue.pop()
        if next in seen:
            continue
        seen.add(next)
        river_size += 1
        valid_paths = get_valid_paths(next, matrix, seen)
        queue.extend(valid_paths)
    result.append(river_size)


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    assert sorted(river_sizes(matrix)) == [1, 2, 2, 2, 5]
    matrix = [
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    ]
    assert sorted(river_sizes(matrix)) == [1, 1, 2, 2, 5, 21]
