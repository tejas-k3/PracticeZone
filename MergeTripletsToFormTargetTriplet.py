# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        triplets.sort()
        a = b = c = 0
        t1, t2, t3 = target
        for x, y, z in triplets:
            if x <= t1 and y <= t2 and z <= t3:
                a = max(a, x)
                b = max(b, y)
                c = max(c, z)
        return [a, b, c] == target
