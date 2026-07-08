class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                row_val = ("row", i, val)
                column_val = ("column", j, val)
                box_val = ("box", i // 3, j // 3, val)

                if row_val in seen or column_val in seen or box_val in seen:
                    return False
                seen.add(row_val)
                seen.add(column_val)
                seen.add(box_val)
        return True