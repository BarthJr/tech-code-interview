# https://leetcode.com/problems/first-bad-version/

# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


def firstBadVersion(n):
    start, end = 1, n
    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return end
