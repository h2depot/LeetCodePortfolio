class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        cnt = 1
        i = 0
        while cnt < x:
            i+=1
            cnt += (2*i + 1)
        if cnt == x:
            return i + 1
        else:
            return i
        