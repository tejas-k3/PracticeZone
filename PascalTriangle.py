""" https://leetcode.com/problems/pascals-triangle
Approach :- To create a this for the ith row and jth
column we simply add jth and (j-1)th column of (i-1)th row. 
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        for rowNum in range(numRows):
            row = [None for _ in range(rowNum + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = sol[rowNum - 1][j - 1] + sol[rowNum - 1][j]

            sol.append(row)

        return sol