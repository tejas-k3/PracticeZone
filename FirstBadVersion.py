""" https://leetcode.com/problems/first-bad-version/
Approach :- Binary :D w
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while(left<right):
            mid = left + int(right-left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return int(left)