# https://leetcode.com/problems/number-of-good-pairs/
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        ans = 0
        for num in nums:
            ans += counts[num]
            counts[num] += 1
        return ans