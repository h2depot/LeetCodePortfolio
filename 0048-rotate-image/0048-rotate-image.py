class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #行列の転置
        limit = len(matrix)
        for i in range(limit):
            for j in range(i, limit):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #行列の左右反転
        for row in matrix:
            row.reverse()
        print(matrix)


        