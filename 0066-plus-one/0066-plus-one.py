class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dilist=[]
        increment = 0
        digits[-1] += 1
        for i, di in enumerate(reversed(digits)):
            if di + increment == 10:
                increment = 1
                dilist.append(0)
            else:
                dilist.append(di + increment)
                increment = 0
        if increment == 1:
            dilist.append(1)
        dilist.reverse()
        return dilist
        