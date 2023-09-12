# https://leetcode.com/problems/number-of-good-ways-to-split-a-string
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftCount = collections.Counter()
        rightCount = collections.Counter(s)
        res = 0
        for c in s:
            leftCount[c] += 1
            rightCount[c] -= 1
            if rightCount[c] == 0:
                del rightCount[c]
            
            if len(leftCount) == len(rightCount):
                res += 1
                
        return res