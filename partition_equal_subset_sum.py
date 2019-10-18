# https://www.lintcode.com/problem/partition-equal-subset-sum/description

# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
# Example:
# Input: nums = [1, 5, 11, 5],
# Output: true
# Explanation:
# two subsets: [1, 5, 5], [11]

"""
>>> Solution().canPartition([1, 5, 11, 5])
True
>>> Solution().canPartition([1, 2, 3, 9])
False
>>> Solution().canPartition([1, 4, 5, 6, 1, 32, 4, 1, 3, 4, 5, 5, 5, 5, 1, 2, 4, 5, 1])
True
"""


class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """

    def canPartition(self, nums):
        memo = dict()
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self._canPartition(nums, 0, 0, total, memo)

    def _canPartition(self, nums, index, partial_sum, total, memo):
        current = f'{index}_{partial_sum}'
        if current in memo:
            return memo[current]
        if partial_sum * 2 == total:
            return True
        elif partial_sum > total // 2 or index >= len(nums):
            return False
        without_get_number = self._canPartition(nums, index + 1, partial_sum, total, memo)
        get_number = self._canPartition(nums, index + 1, partial_sum + nums[index], total, memo)
        memo[current] = without_get_number or get_number
        return memo[current]
