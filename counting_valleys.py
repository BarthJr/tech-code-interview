# https://www.hackerrank.com/challenges/counting-valleys/problem

"""
>>> countingValleys('DDUUUUDD')
1
>>> countingValleys('UDDDUDUU')
1

"""


def countingValleys(s):
    count, count_valleys = 0, 0
    for i, w in enumerate(s):
        if w == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and s[i] == 'U':
            count_valleys += 1
    return count_valleys
