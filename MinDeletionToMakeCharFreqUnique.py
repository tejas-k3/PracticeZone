# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, result, used = collections.Counter(s), 0, set()
        for ch, freq in count.items():
            while freq > 0 and freq in used:
                freq -= 1
                result += 1
            used.add(freq)
        return result