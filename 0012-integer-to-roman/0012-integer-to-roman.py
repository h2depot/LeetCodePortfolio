class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'),(50,'L'), (90,'XC'), (100,'C'), (400,'CD'),(500,'D'), (900,'CM'),(1000,'M')]
        ans = ""
        while num > 0:
            print(num)
            max = 1
            idx = 0
            for i in range(len(dict)):
                key = dict[i][0]
                if max <= key and key <= num:
                    max = key
                    idx = i
            num -= max
            ans += dict[idx][1]
        return ans                   
            
        