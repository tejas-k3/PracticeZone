# https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = [c for c in s.lower() if c.isalnum()]
        return new_s == new_s[::-1]