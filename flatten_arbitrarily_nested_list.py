"""
>>> flatten([1, [4, [6, [5]]]])
[1, 4, 6, 5]
>>> flatten([[1, 1], 2, [1, 1]])
[1, 1, 2, 1, 1]
"""


def flatten(lst):
    result = []
    for element in lst:
        if type(element) is type([]):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result
