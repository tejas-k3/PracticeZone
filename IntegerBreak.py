# https://leetcode.com/problems/integer-break
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        @cache
        def dp(num):
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            return ans
        if n <= 3:
            return n - 1
        return dp(n)