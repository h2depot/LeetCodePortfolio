class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = ""
        tmp = str(bin(n))
        for i in range(34-len(tmp)):
            string += "0"
        print(string)
        string += tmp[2:]
        string2 = ""
        for i,c in enumerate(reversed(string)):
            string2 += c
        print(string)
        print(string2)
        return int(string2, 2)
        