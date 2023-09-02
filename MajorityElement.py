# https://leetcode.com/problems/majority-element
# This is a clever thing cited @
# https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal, counter = nums[0], 1
        length = len(nums)
        for i in range(1, length):
            if maxVal == nums[i]:
                counter+=1
            else:
                counter-=1
            if counter == 0:
                counter+=1
                maxVal = nums[i]
        return maxVal