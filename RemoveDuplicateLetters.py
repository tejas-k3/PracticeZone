# https://leetcode.com/problems/remove-duplicate-letters/
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occ = {}
        stack = []
        visited = set()
        for i in range(len(s)):
            last_occ[s[i]] = i
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
                
        return ''.join(stack)