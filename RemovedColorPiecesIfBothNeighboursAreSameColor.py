# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color
class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        length = len(colors)
        alice, bob = 0, 0
        if length < 3:
            return False
        for i in range(0, length-2):
            if colors[i] == 'A' and colors[i+1] == 'A' and colors[i+2] == 'A':
                alice+=1
            if colors[i] == 'B' and colors[i+1] == 'B' and colors[i+2] == 'B':
                bob+=1
        return alice > bob