# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        startingIndex = 0
        charIndexes = {}
        for currentIndex in range(n):
            if s[currentIndex] in charIndexes:
                startingIndex = max(charIndexes[s[currentIndex]], startingIndex)
            ans = max(ans, currentIndex - startingIndex + 1)
            charIndexes[s[currentIndex]] = currentIndex + 1
        return ans