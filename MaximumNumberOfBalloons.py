# https://leetcode.com/problems/maximum-number-of-balloons/
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])