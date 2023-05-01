# https://leetcode.com/problems/longest-repeating-character-replacement/
# Binary search + sliding window
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lo = 1
        hi = len(s)+1
        while lo!=hi-1:
            mid = (lo+hi)/2
            if self.makeValidSubstring(s, mid, k):
                lo = mid
            else:
                hi = mid
        return lo

    def makeValidSubstring(self, s, mid, k):
        freq_map = {}
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            if end + 1 - start > mid:
                freq_map[s[start]] -= 1
                start += 1
            max_frequency = max(max_frequency, freq_map[s[end]])
            if mid - max_frequency <= k:
                return True
        return False