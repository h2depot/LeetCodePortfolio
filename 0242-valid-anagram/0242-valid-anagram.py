class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for j in t:
            if j not in dict:
                return False
            else:
                dict[j] -= 1
            if dict[j] < 0:
                return False
        if sum(dict.values()) > 0:
            return False
        return True
        