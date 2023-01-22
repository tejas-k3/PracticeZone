""" https://leetcode.com/problems/valid-parentheses
Approach :- Form a deque and just do check before insertion 
of the ending character for each type and pop and check for len.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        try:
            for i in s:
                if i =='(' or i=='[' or i =='{':
                    stack.append(i)
                elif i ==')' and stack.pop()=='(':
                    continue
                elif i =='}' and stack.pop()=='{':
                    continue
                elif i ==']' and stack.pop()=='[':
                    continue
                else:
                    return False
            if len(stack)==0:
                return True
            return False
        except:
            return False