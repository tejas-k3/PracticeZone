class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: straa
        """
        s_char = dict()
        for char in s:
          if not s_char.get(char):
            s_char[char] = 1
          else:
            s_char[char]+=1
        for char in t:
          if char in s_char:
            s_char[char] -= 1
            if s_char[char]== -1:
              return char
            continue
          return char