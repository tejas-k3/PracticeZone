# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output