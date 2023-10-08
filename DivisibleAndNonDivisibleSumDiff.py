# https://leetcode.com/contest/weekly-contest-366/problems/divisible-and-non-divisible-sums-difference/
class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total = 0
        for i in range(1, n+1):
            if i%m != 0:
                total += i
            else:
                total-=i
        return total