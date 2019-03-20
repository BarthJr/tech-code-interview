# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part of the result is returned.
"""
>>> mySqrt(8)
2
>>> mySqrt(1)
1
>>> mySqrt(0)
0
"""


def mySqrt(x: int) -> int:
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 <= x < (mid + 1) ** 2:
            return mid
        elif x < mid ** 2:
            right = mid
        else:
            left = mid + 1
