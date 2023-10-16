# https://leetcode.com/problems/pascals-triangle-ii
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row