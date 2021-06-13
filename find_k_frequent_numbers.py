"""
>>> find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)
[11, 12]
>>> find_k_frequent_numbers([5, 12, 11, 3, 11], 2)
[12, 11]
"""


from heapq import *

# Time O(N + N * logK) | Space O(N)
def find_k_frequent_numbers(nums, k):
  minHeap = []
  frequencies = {}

  for num in nums:
      frequencies[num] = frequencies.get(num, 0) + 1

  for num, frequency in frequencies.items():
      heappush(minHeap, (frequency, num))

      if len(minHeap) > k:
          heappop(minHeap)

  return [num for frequency, num in minHeap]
