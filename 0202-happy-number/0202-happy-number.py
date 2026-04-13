class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while(1):
            nlist = list(str(n))
            nlist2 = [0] * len(nlist)
            for i in range(len(nlist)):
                nlist2[i] = int(nlist[i]) * int(nlist[i])
            print(nlist2)

            n = 0
            for j, num in enumerate(nlist2):
                n += num
            if n not in dict:
                dict[n] = True
            else:
                return False
            if n == 1:
                return True
        