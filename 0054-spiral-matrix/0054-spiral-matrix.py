class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        cnt = 0
        i_row = 0
        i_column = 0
        f_row = len(matrix)-1
        f_column = len(matrix[0])-1
        while  len(ans) != len(matrix) * len(matrix[0]):
            if cnt % 4 == 0:
                for i in range(i_column, f_column+1):
                    ans.append(matrix[i_row][i])
                cnt += 1
                i_row += 1

            elif cnt % 4 == 1:
                for i in range(i_row, f_row+1):
                    ans.append(matrix[i][f_column])
                cnt += 1
                f_column -= 1

            elif cnt % 4 == 2:
                for i in range(f_column, i_column-1, -1):
                    ans.append(matrix[f_row][i])
                cnt += 1
                f_row -= 1
            else:
                for i in range(f_row, i_row-1, -1):
                    ans.append(matrix[i][i_column])
                cnt += 1
                i_column += 1  
            print(ans)
        return ans             
        