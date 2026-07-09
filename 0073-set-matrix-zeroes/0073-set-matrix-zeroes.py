class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in columns:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        