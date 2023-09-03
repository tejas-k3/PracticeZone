# https://leetcode.com/problems/next-permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # use binary search because it's descending order
        if i > 0:
            left, right = i, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[i-1] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            nums[i-1], nums[left-1] = nums[left-1], nums[i-1]
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1