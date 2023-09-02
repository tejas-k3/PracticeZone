# https://leetcode.com/problems/can-place-flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        if n == 0:
            return True
        lenFB = len(flowerbed)
        for i in range(lenFB):
            if flowerbed[i] == 0:
                emptyLeftPot = (i == 0) or (flowerbed[i - 1] == 0)
                emptyRightLot = (i == lenFB - 1) or (flowerbed[i + 1] == 0)
                if emptyLeftPot and emptyRightLot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return False