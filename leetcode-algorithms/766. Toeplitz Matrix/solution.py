# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row_len = len(matrix[0])
        col_len = len(matrix)
        for i in range(col_len-1):
            if matrix[i][0:row_len-1] != matrix[i+1][1:row_len]:
                return False
        return True

