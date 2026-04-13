class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        strs.sort()
        a = strs[0]
        b = strs[-1]
        N = len(a) if len(a) < len(b) else len(b)
        for i in range(N):
            if a[i] == b[i]:
                pref += a[i]
            else:
                return pref
        return pref
