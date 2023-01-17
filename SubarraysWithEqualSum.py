""" https://leetcode.com/contest/biweekly-contest-86/problems/find-subarrays-with-equal-sum/
Approach :- Save sum of consecutive elements as key value pair
in a dict
"""
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        result = {}
        length = len(nums)
        for i in range(0, length-1):
            if (nums[i]+nums[i+1]) in result:
                    # result[nums[i]+nums[i+1]]+=1
                return True
            else:
                result[nums[i]+nums[i+1]]=1
        return False