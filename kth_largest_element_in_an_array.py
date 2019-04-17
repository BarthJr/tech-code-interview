# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
>>> findKthLargest([3, 2, 1, 5, 6, 4], 2)
5
>>> findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
4
>>> findKthLargest([2], 1)
2
"""
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    return sorted(nums)[-k]
