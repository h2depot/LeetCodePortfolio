class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prev = 0
        sum = 0
        for i, c in enumerate(reversed(s)):
            c_n = dict[c]
            if prev > c_n:
                sum -= c_n
            else:
                sum += c_n
            prev = c_n
        return sum
