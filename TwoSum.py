""" https://leetcode.com/problems/two-sum
Appraoch :- Iterate through the list and maintain a dictionary 
with val as key and index as value, check for diff with target val
for current element and if exists, return the values as list.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        justVal = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in justVal:
                return [justVal[diff], i]
            justVal[n] = i