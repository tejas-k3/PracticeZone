# https://leetcode.com/problems/frog-jump/
class Solution:
    def canCross(self, stones):
        mark = {}
        dp = [[-1] * 2001 for _ in range(2001)]
        def solve(index, prevJump):
            if index == len(stones) - 1:
                return True
            if dp[index][prevJump] != -1:
                return dp[index][prevJump] == 1
            ans = False
            for nextJump in range(prevJump - 1, prevJump + 2):
                if nextJump > 0 and stones[index] + nextJump in mark:
                    ans = ans or solve(mark[stones[index] + nextJump], nextJump)
            dp[index][prevJump] = 1 if ans else 0
            return ans
        for i in range(len(stones)):
            mark[stones[i]] = i
        for i in range(2000):
            dp[i] = [-1] * 2001
        
        return solve(0, 0)
