# https://leetcode.com/problems/knight-dialer/
class Solution:
    def knightDialer(self, n):
        transitions = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        dp = [[0 for _ in range(10)] for _ in range(n)]
        
        # base case
        for i in range(10):
            dp[-1][i] = 1
        
        for i in range(n-2, -1, -1):
            for d in range(10):
                for reach_d in transitions[d]:
                    dp[i][d] = (dp[i][d] + dp[i+1][reach_d]) % (10**9+7)
        
        ans = 0
        for s in dp[0]:
            ans = (ans + s) % (10**9+7)
        return ans