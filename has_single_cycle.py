# You are given an array of integers. Each integer represents a jump of its value in the array.
# For instance, the integer 2 represents a jump of 2 indices forward in the array;
# the integer -3 represents a jump of 3 indices backward in the array. If a jump spills past the array's bounds,
# it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array.
# Similarly, a jump of 1 at the last index in the array brings us to index 0.
# Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
# A single cycle occurs if, starting at any index in the array and following the jumps,
# every element is visited exactly once before landing back on the starting index.

"""
>>> hasSingleCycle([2, 3, 1, -4, -4, 2])
True
>>> hasSingleCycle([1, 1, 1, 1, 2])
False
"""


def hasSingleCycle(array):
    START_IDX = 0
    num_elements_visited = 0
    current_idx = START_IDX

    while num_elements_visited < len(array):
        if num_elements_visited > 0 and current_idx == START_IDX:
            return False
        num_elements_visited += 1
        current_idx = get_current_idx(current_idx, array)

    return current_idx == START_IDX


def get_current_idx(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)

    return next_idx
