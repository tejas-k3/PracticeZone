# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}
        def dfs(row, col, prevVal):
            if (row < 0 or col < 0 or 
            row == ROWS or col == COLS or
            matrix[row][col] <= prevVal):
                return 0
            if (row, col) in dp:
                return dp[(row, col)]
            res = 1
            res = max(res, 1 + dfs(row + 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row -1 , col, matrix[row][col]))
            res = max(res, 1 + dfs(row, col - 1, matrix[row][col]))
            dp[(row, col)] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())