# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

"""
Another sol of this as done in 2Sum Sorted!
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = {}
        nums.sort()
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = val1 + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
        return res

"""