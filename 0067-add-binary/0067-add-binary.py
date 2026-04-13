class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        increment = 0
        sum = ""
        while i < len(a) or i < len(b):
            ai = int(a[-i-1] if i < len(a) else 0)
            bi = int(b[-i-1] if i < len(b) else 0)
            print(ai + bi + increment )
            if ai + bi + increment == 3:
                sum+="1"
                increment = 1
            elif ai + bi + increment == 2:
                sum+="0"
                increment = 1
            elif ai + bi + increment == 1:
                sum+="1"
                increment = 0
            elif ai + bi + increment == 0:
                sum+="0"
                increment = 0
            i+=1
        if increment == 1:
            sum+="1"
        sum_r = "".join(reversed(sum))
        return sum_r
                

            
        