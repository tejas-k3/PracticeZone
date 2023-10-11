# https://leetcode.com/problems/number-of-flowers-in-full-bloom
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        # For each person's timestamp see what all flowers are falling 
        starts = []
        ends = []
        ans = []
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        starts.sort()
        ends.sort()
        # Find index of where time is
        # For that index how many bloomed
        # flowers, how many closed flowers
        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)
        return ans