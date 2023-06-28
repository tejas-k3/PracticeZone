# https://leetcode.com/problems/spiral-matrix/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
        direction = 1 # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n): # move horizontally
                j += direction
                output.append(matrix[i][j])
            m-= 1
            for _ in range(m): # move vertically
                i += direction
                output.append(matrix[i][j])
            n-=1
            direction *= -1 # flip direction
        return output