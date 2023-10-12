# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low, high = 0, len(arr)-1
        while low < high:
            mid = high + (low - high)/2
            print(arr[low], arr[high], arr[mid])
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
                low = mid
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
                high = mid