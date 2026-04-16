class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = str(bin(n))
        cnt = 0
        for i in range(len(string)):
            if string[i] == "1":
                cnt += 1
        return cnt
        