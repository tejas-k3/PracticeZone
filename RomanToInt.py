""" https://leetcode.com/problems/roman-to-integer/
Approach :- Basic comparison 
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number=0
        if 'IV' in s:
            number+=4
            s = s.replace('IV', ' ')
        if 'IX' in s:
            number+=9
            s = s.replace('IX', ' ')
        if 'XL' in s:
            number+=40
            s = s.replace('XL', ' ')
        if 'XC' in s:
            number+=90
            s = s.replace('XC', ' ')
        if 'CD' in s:
            number+=400
            s = s.replace('CD', ' ')
        if 'CM' in s:
            number+=900
            s = s.replace('CM', ' ')
        print(s)
        for num in s:
            if num == 'I':
                number+=1
            if num == 'V':
                number+=5
            if num == 'X':
                number+=10
            if num == 'L':
                number+=50
            if num == 'C':
                number+=100
            if num =='D':
                number+=500
            if num =='M':
                number+=1000
        return number