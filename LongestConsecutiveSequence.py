# https://leetcode.com/problems/longest-consecutive-sequence/
# Make a set and iterate through it checking for longest seq
class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest_seq = 0
        
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_seq = 1
                
                while current_num+1 in nums_set:
                    current_num += 1
                    current_seq += 1
                
                longest_seq = max(longest_seq, current_seq)
        
        return longest_seq