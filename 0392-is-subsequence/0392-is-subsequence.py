class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        if s == "":
            return True
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True
            i +=1
        return False