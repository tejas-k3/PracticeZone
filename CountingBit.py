"""
https://leetcode.com/problems/counting-bits/description/
Approach - CHEATING, just convert using internal function
Can do //2 tho!
"""

"""
Better approach with O(N)
    def countBits(self, n):
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = self.solve(i, res)
        return res

    def solve(self, n, memo):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if memo[n] != 0:
            return memo[n]
        if n % 2 == 0:
            memo[n] = self.solve(n // 2, memo)
            return memo[n]
        else:
            memo[n] = 1 + self.solve(n // 2, memo)
            return memo[n]
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        nums=[]
        for i in range(n+1):
            i = ('{:032b}'.format(i))
            val = 0
            for s in i:
                if s=='1':
                    val+=1
            nums.append(val)
        return nums