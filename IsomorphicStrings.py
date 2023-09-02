# https://leetcode.com/problems/isomorphic-strings/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLen = len(s)
        tLen = len(t)
        if sLen != tLen :
            return False
        sCharSet = {}
        tCharSet = {}
        for idx in range(sLen):
            if s[idx] in sCharSet or t[idx] in tCharSet:
                if (sCharSet.get(s[idx]) == t[idx] and 
                tCharSet.get(t[idx]) == s[idx]):
                    continue
                return False
            sCharSet[s[idx]]= t[idx]
            tCharSet[t[idx]]= s[idx]
        return True