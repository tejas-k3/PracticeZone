""" https://leetcode.com/problems/intersection-of-two-arrays-ii/
Approach :- Iterate through the smaller list and if element is present in both,
add it into a dict with its frequency & late form a list from dict and return it
"""
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1 = len(nums1)
        size2 = len(nums2)
        ele = dict()
        if size2 >= size1:
            # Iterate through s2 and then compare with s1
            for i in nums1:
                if i not in ele:
                    ele[i]=1
                else:
                    ele[i]+=1
            nums1.clear()
            print(ele)
            for n in nums2:
                if n in ele and ele[n]>0:
                    ele[n]-=1
                    nums1.append(n)
                print(ele)
            
            return nums1
        else:
            # Iterate through s2 and then compare with s1
            for i in nums2:
                if i not in ele:
                    ele[i]=1
                else:
                    ele[i]+=1
            nums2.clear()
            for n in nums1:
                if n in ele and ele[n]>0:
                    ele[n]-=1
                    nums2.append(n)
            return nums2