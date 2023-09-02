# https://leetcode.com/problems/next-greater-element-i
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        mapping = {}
        
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)
            
        while stack:
            mapping[stack.pop()] = -1
            
        for n in nums1:
            res.append(mapping[n])

        return res