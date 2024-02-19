# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))