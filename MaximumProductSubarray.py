# https://leetcode.com/problems/maximum-product-subarray/description/
# Simplest 1D DP problem I've ever solved
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxSoFar = nums[0]
        minSoFar = nums[0]
        result = maxSoFar
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, maxSoFar * curr, minSoFar * curr)
            minSoFar = min(curr, maxSoFar * curr, minSoFar * curr)
            maxSoFar = tempMax
            result = max(maxSoFar, result)
        return result