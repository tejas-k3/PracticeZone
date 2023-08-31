# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Define an infinite value
        INF = int(1e9)
        dp = [INF] * (n + 1)
        # Base Case
        dp[0] = 0
        for i in range(n + 1):
            # Calculate the leftmost position reachable by the current tap
            tapStart = max(0, i - ranges[i])
            # Calculate the rightmost position reachable by the current tap
            tapEnd = min(n, i + ranges[i])
            for j in range(tapStart, tapEnd + 1):
                dp[tapEnd] = min(dp[tapEnd], dp[j] + 1)
        return -1 if dp[n] == INF else dp[n]