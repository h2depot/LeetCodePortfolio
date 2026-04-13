class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = float('inf')
        prof = 0

        for i in prices:
            if i < min:
                min = i
            if i - min > prof:
                prof = i-min
        return prof