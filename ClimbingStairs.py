""" https://leetcode.com/problems/climbing-stairs/description/
Approach :-
It's a DP Problem, identical to the fibonacci series construction
Cover base solutions (n=1, n=2) and return for desired value by
bottom to top approach.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        elif n==2:
            return 2
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]