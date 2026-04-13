class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        idx = 0
        for i in range(len(s)):
            if s[i] not in dict:
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]
            else:
                if dict[s[i]] != t[i]:
                    return False
        return True
            
            
            