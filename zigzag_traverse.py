# Write a function that takes in a two-dimensional array and returns a one-dimensional array of all the array's elements
# in zigzag order. Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element,
# and proceeds in a zigzag pattern all the way to the bottom right corner.

def zigzagTraverse(array):
    lin = 0
    col = 0
    L = len(array) - 1
    C = len(array[0]) - 1
    is_going_down = True
    result = []
    while not out_of_bounds(lin, col, array):
        result.append(array[lin][col])
        if is_going_down:
            if col == 0 or lin == L:
                is_going_down = False
                if lin == L:
                    col += 1
                else:
                    lin += 1
            else:
                lin += 1
                col -= 1
        else:
            if lin == 0 or col == C:
                is_going_down = True
                if col == C:
                    lin += 1
                else:
                    col += 1
            else:
                lin -= 1
                col += 1

    return result


def out_of_bounds(lin, col, array):
    L = len(array) - 1
    C = len(array[0]) - 1
    return lin < 0 or lin > L or col < 0 or col > C


if __name__ == '__main__':
    matrix = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]
    ]
    assert zigzagTraverse(matrix) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
