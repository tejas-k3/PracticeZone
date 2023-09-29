# https://leetcode.com/problems/monotonic-array
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not {cmp(i, j) for i, j in zip(nums, nums[1:])} >= {1, -1}