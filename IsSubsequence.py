# https://leetcode.com/problems/is-subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        sLen, tLen = len(s), len(t)
        if sLen == 0:
            return True
        elif sLen > tLen:
            return False
        for i in range(tLen):
            if t[i] == s[j]:
                j+=1
            if j == sLen:
                return True
        return False