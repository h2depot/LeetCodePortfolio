class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ans = ""
        for i in range(len(words)):
            ans += words[-i-1]
            if i != len(words)-1:
                ans += " "
        return ans
