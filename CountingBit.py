"""
https://leetcode.com/problems/counting-bits/description/
Approach - CHEATING, just convert using internal function
Can do //2 tho!
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