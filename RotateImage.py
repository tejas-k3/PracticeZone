""" https://leetcode.com/problems/rotate-image
Appraoch :- It's just there in function def :)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Step 1 Transpose
        Step 2 Switch the positions row-wise for 90Degree
        """
        n = len(matrix)
        c = int((n+1) / 2)
        f = int(n / 2)
        for x in range(c):
            for y in range(f):
                matrix[x][y] = matrix[x][y] ^ matrix[n-1-y][x]
                matrix[n-1-y][x] = matrix[x][y] ^ matrix[n-1-y][x]
                matrix[x][y] = matrix[x][y] ^ matrix[n-1-y][x]
                matrix[n-1-y][x] = matrix[n-1-y][x] ^ matrix[n-1-x][n-1-y]
                matrix[n-1-x][n-1-y] = matrix[n-1-y][x] ^ matrix[n-1-x][n-1-y]
                matrix[n-1-y][x] = matrix[n-1-y][x] ^ matrix[n-1-x][n-1-y]
                matrix[n-1-x][n-1-y] = matrix[n-1-x][n-1-y]^matrix[y][n-1-x]
                matrix[y][n-1-x] = matrix[n-1-x][n-1-y]^matrix[y][n-1-x]
                matrix[n-1-x][n-1-y] = matrix[n-1-x][n-1-y]^matrix[y][n-1-x]