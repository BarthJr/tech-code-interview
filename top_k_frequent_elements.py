# Given a non-empty array of integers, return the k most frequent elements.

"""
>>> top_k_frequent([3, 1, 1, 1, 2, 2], 2)
[1, 2]
>>> top_k_frequent([1], 1)
[1]
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    return heapq.nlargest(k, counter.keys(), key=counter.get)
