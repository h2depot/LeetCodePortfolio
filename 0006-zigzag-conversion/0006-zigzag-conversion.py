class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [""] * numRows
        pointer = 0
        direction = 1
        for char in s:
            rows[pointer] += char
            if pointer == 0:
                direction = 1
            if pointer == numRows-1:
                direction = -1
            pointer += direction
        
        return "".join(rows)
                
