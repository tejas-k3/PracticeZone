""" https://leetcode.com/problems/missing-number
Appraoch :- Just maths
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = int((len(nums)*(len(nums)+1))/2)
        for i in nums:
            val-=i
        return val