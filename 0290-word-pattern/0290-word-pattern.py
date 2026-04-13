class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict = {}
        s_sp = s.split()
        if len(s_sp) != len(pattern):
            return False
        for i in range(len(s_sp)):
            if pattern[i] not in dict and s_sp[i] in dict.values():
                return False
            if pattern[i] not in dict:
                dict[pattern[i]] = s_sp[i]
            else:
                if dict[pattern[i]] != s_sp[i]:
                    return False
        return True
            
        