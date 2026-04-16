class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = []
        array.append(1)
        array.append(2)
        for i in range(2,n):
            array.append(array[i-1]+array[i-2])
        return array[n-1]