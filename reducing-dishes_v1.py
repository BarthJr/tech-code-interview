# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
#
# Like-time coefficient of a dish is defined as the time taken to cook that dish
# including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]
#
# Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.
#
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

"""
>>> Solution().maxSatisfaction([-1,-8,0,5,-9])
14
>>> Solution().maxSatisfaction([4,3,2])
20
>>> Solution().maxSatisfaction([-1,-4,-5])
0
>>> Solution().maxSatisfaction([-2,5,-1,0,3,-3])
35
"""
from typing import List


class Solution:
    # O(n^2) time | O(1) space
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        factor = 1
        maxSumLikeTime = 0

        while factor <= len(satisfaction):
            time = factor
            partialSumLikeTime = 0
            for i in reversed(range(len(satisfaction) - factor, len(satisfaction))):
                partialSumLikeTime += satisfaction[i] * time
                time -= 1
            if partialSumLikeTime < maxSumLikeTime:
                break
            maxSumLikeTime = partialSumLikeTime
            factor += 1

        return maxSumLikeTime
