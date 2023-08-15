# https://leetcode.com/problems/unique-paths
class Solution:
    # Memoization
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

    # Tabulation
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    # Space optimised
    def uniquePaths(self, m, n):
        dp = [1]*n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j-1]
        return dp[-1]