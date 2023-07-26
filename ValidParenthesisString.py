# https://leetcode.com/problems/valid-parenthesis-string
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = high = 0
        for char in s:
            low += 1 if char == '(' else -1
            high += 1 if char != ')' else -1
            if high < 0: break
            low = max(low, 0)
        return low == 0
