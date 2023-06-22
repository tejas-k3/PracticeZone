# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums):
        seq = [nums[0]]
        for num in nums[1:]:
            if num > seq[-1]:
                seq.append(num)
            else:
                # Find the first element in seq that is greater than or equal to num
                i = 0
                while num > seq[i]:
                    i += 1
                seq[i] = num
        return len(seq)