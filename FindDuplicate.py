# https://leetcode.com/problems/find-the-duplicate-number
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeated_num = 1
        total_sum = 0
        for num in nums:
            # total_sum+=abs(num)
            if nums[abs(num)-1] < 0:
                repeated_num = abs(num)
                return repeated_num
            nums[abs(num)-1]*=-1
        """
        Additional code to tell missing number
        """
        # print(total_sum)
        # total_sum-=repeated_num
        # n = len(nums)
        # val = 0
        # if n%2 == 0:
        #     val=n/2
        #     val*=n
        #     val+=n/2
        # else:
        #     val =(n+1)/2
        #     val*=n
        # print(val)
        # print(total_sum)
        # return val-total_sum