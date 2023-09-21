# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        curr_sum, max_len = 0, -1
        start_idx = 0
        num_len = len(nums)
        for end_idx in range(num_len):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                max_len = max(max_len, end_idx - start_idx + 1)
        return num_len - max_len if max_len != -1 else -1
