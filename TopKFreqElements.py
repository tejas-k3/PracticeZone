""" https://leetcode.com/problems/top-k-frequent-elements/
Approach :- Iterate through the list and populate a dict with value:frequency pair
iterate through dictonary where freq is greater than or equal to K value and append
it into a list.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = dict()
        ans = list()
        for i in nums:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
        for i in range(k):
            t = max(x, key=x.get)
            ans.append(t)
            del x[t]
        return ans