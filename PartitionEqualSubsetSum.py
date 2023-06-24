# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        subSetSum = totalSum // 2
        n = len(nums)
        dp = [[False] * (subSetSum+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(subSetSum+1):
                if j < curr:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[n][subSetSum]