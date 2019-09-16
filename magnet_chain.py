# Find the total number of chains of length n that can be formed in the grid such that:
#  1. Every column of the grid contains one and only one link
#  2. The next chain cell can be one unit Up or Down or Inline
#  3. Chain links can only be inside the grid
#  4. Every chain starts at the bottom-left grid

"""
>>> chain(2)
2
>>> chain(3)
5
>>> chain(4)
13
>>> chain(5)
35
>>> chain(6)
96
"""


def chain(size):
    def _chain(i, j, size):
        if i < 0 or i > size:
            return 0
        if j == size:
            return 1
        j += 1
        a = _chain(i - 1, j, size)
        b = _chain(i, j, size)
        c = _chain(i + 1, j, size)
        return a + b + c

    return _chain(0, 0, size - 1)
