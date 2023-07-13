# https://leetcode.com/problems/non-overlapping-intervals/
# GREEDY SOL BRAINFUK
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = float('-inf')
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        return ans