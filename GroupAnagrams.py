""" https://leetcode.com/problems/group-anagrams/
Approach :- Assign prime value to each char, iterate through give group of string & multiply 
corresponding char values together to form a result value and store the string with the result value
as the key in a dictionary with key : list pair where string is appended to the list 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        primes = {'a': 2, 'b': 3, 'c': 5, 'd': 7,  'e': 11, 'f': 13, 'g': 17, 'h': 19, 
                  'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 
                  'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 
                  'w': 83, 'x': 89, 'y': 97, 'z': 101}
        
        subLists = {}
        for string in strs:
            product = 1
            for character in string:
                product = primes[character] * product
            if product in subLists.keys():
                listA = subLists[product]
                listA.append(string)
                subLists[product] = listA
            else:
                subLists[product] = [string]
        listToReturn = []
        for value in subLists.keys():
            listToReturn.append(subLists[value])
            
        return listToReturn