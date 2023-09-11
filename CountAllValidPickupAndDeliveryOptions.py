# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, mod = 1, 10**9 + 7
        for i in xrange(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) / 2 % mod
        return res