# You are given a non-empty array of arrays. Each subarray holds three integers and represents a disk.
# These integers denote each disk's width, depth, and height, respectively.
# Your goal is to stack up the disks and to maximize the total height of the stack.
# A disk must have a strictly smaller width, depth, and height than any other disk below it.
# Write a function that returns an array of the disks in the final stack,
# starting with the top disk and ending with the bottom disk. Note that you cannot rotate disks; in other words,
# the integers in each subarray must represent [width, depth, height] at all times.
# Assume that there will only be one stack with the greatest total height.

"""
>>> diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]])
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]
"""


def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    sequences = [None for _ in disks]
    heights = [disk[2] for disk in disks]

    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(0, i):
            other_disk = disks[j]
            if validate_disks(other_disk, current_disk):
                if heights[i] < heights[j] + current_disk[2]:
                    heights[i] = heights[j] + current_disk[2]
                    sequences[i] = j

    max_height_idx = heights.index(max(heights))

    return disks_max_height(max_height_idx, disks, sequences)


def disks_max_height(max_height_idx, disks, sequences):
    result = []
    while max_height_idx is not None:
        result.append(disks[max_height_idx])
        max_height_idx = sequences[max_height_idx]
    return list(reversed(result))


def validate_disks(other_disk, current_disk):
    return other_disk[0] < current_disk[0] and other_disk[1] < current_disk[1] and other_disk[2] < current_disk[2]
