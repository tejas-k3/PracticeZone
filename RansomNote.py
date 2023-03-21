""" https://leetcode.com/problems/ransom-note/
Approach :- Just check for subset and count of characters
"""

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        A = set(ransomNote)
        B = set(magazine)
        if A.issubset(B):
            # CHECK CHAR LIMITATION 
            ransomNote = Counter(ransomNote)
            magazine = Counter(magazine)
            for key in ransomNote:
                if magazine[key] < ransomNote[key]:
                    return False
            return True
        return False