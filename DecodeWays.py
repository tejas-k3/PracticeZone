# https://leetcode.com/problems/decode-ways/
# 1D DP, ITERATIVE APPROACH
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        twoBack = 1
        oneBack = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = oneBack
            twoDigit = int(s[i - 1: i + 1])
            if twoDigit >= 10 and twoDigit <= 26:
                current += twoBack
            twoBack = oneBack
            oneBack = current
        return oneBack