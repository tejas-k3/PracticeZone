"""
https://leetcode.com/problems/container-with-most-water/
Approach :-
Iterate through the given list to find maximum area.
Using two pointer method one at left, one at right, move 
if next value is higher than current value towards center.
Update maxarea value as fitting and return.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea