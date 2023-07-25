# https://leetcode.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {char: index for index, char in enumerate(s)}
        j = anchor = 0
        ans = []
        for index, char in enumerate(s):
            j = max(j, last[char])
            if index == j:
                ans.append(index - anchor + 1)
                anchor = index + 1
        return ans