# https://leetcode.com/contest/weekly-contest-366/problems/minimum-processing-time/
class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        tasks.sort()
        processorTime.sort()
        ans = -1
        pros = len(processorTime)
        length = pros*4
        index, t = pros, 0
        for i in range(length):
            if t%4 == 0:
                index-=1
                t==0
            # print('i ', i, ' index ', index, ' values are ',processorTime[index], ' ',tasks[i])
            ans = max(ans, processorTime[index]+tasks[i])
            t+=1
            
        return ans
