# https://www.hackerrank.com/challenges/counting-valleys/problem

"""
>>> countingValleys('DDUUUUDD')
1
>>> countingValleys('UDDDUDUU')
1

"""


def countingValleys(path):
    UPHILL = 'U'
    DOWNHILL = 'D'
    sea_level, number_valleys = 0, 0
    for i, step in enumerate(path):
        path_elements = {UPHILL: 1, DOWNHILL: -1}
        sea_level += path_elements[step]
        if sea_level == 0 and path[i] == UPHILL:
            number_valleys += 1
    return number_valleys
