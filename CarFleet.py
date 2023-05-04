# https://leetcode.com/problems/car-fleet/
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t