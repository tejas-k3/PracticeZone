# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        firstValue = cost[0]
        secondValue = cost[1]
        totalCosts = len(cost)
        for i in range(2, totalCosts):
            temp = secondValue
            secondValue = cost[i]+min(firstValue, secondValue)
            firstValue = temp
        return min(firstValue, secondValue)