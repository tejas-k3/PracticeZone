""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Appraoch :-
Iterate through the list, track low & high at each element & respective difference as profit
Rby initializing low and high with uppper/lower bounds of given conditions, return the profit at the end.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low, high = 1000000, -1
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = -1
            if prices[i] > high:
                high = prices[i]
            if high - low > profit:
                profit = high - low
        return profit